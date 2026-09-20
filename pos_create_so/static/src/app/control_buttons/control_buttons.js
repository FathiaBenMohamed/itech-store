/** @odoo-module **/

import { ControlButtons } from '@point_of_sale/app/screens/product_screen/control_buttons/control_buttons'
import { patch } from '@web/core/utils/patch'
import { _t } from '@web/core/l10n/translation'
import {
  ConfirmationDialog,
  AlertDialog,
} from '@web/core/confirmation_dialog/confirmation_dialog'
import { useService } from '@web/core/utils/hooks'
import { SelectCreateDialog } from '@web/views/view_dialogs/select_create_dialog'

patch(ControlButtons.prototype, {
  setup() {
    super.setup()
    this.dialogService = useService('dialog')
    this.orm = this.env.services.orm
    this.pos = this.env.services.pos
  },

  onClickQuotation() {
    const context = {
      search_default_salesperson: 1,
    }
    if (this.partner) {
      context['search_default_partner_id'] = this.partner.id
    }
    let domain = [
      ['state', '!=', 'cancel'],
      ['invoice_status', '!=', 'invoiced'],
      ['currency_id', '=', this.pos.currency.id],
    ]
    if (this.pos.getOrder()?.getPartner()) {
      domain = [
        ...domain,
        [
          'partner_id',
          'any',
          [['id', 'child_of', [this.pos.getOrder().getPartner().id]]],
        ],
      ]
    }
    if (this.pos.cashier._role !== 'manager') {
      domain = [...domain, ['user_id', '=', this.pos.cashier.user_id.id]]
    }
    this.dialog.add(SelectCreateDialog, {
      resModel: 'sale.order',
      noCreate: true,
      multiSelect: false,
      domain,
      context: context,
      onSelected: async (resIds) => {
        await this.pos.onClickSaleOrder(resIds[0])
      },
    })
  },

  async clickCreateSaleOrder() {
    const order = this.pos.selectedOrder
    if (!order) {
      this.dialogService.add(AlertDialog, {
        title: _t('Missing Order'),
        body: _t('No active order found.'),
      })
      return
    }

    const partner = order.partner_id
    if (!partner?.id) {
      this.dialogService.add(AlertDialog, {
        title: _t('Missing Customer'),
        body: _t('Select a customer.'),
      })
      return
    }

    const lines = order.lines || []
    if (!lines.length) {
      this.dialogService.add(AlertDialog, {
        title: _t('Missing Products'),
        body: _t('There are no products in the order.'),
      })
      return
    }

    const orderDetails = {
      partner_id: partner.id,
      lines: lines.map((line) => {
        const product = line.product || line.product_id || line.data?.product
        return {
          product_id: product?.id || 0,
          name: product?.display_name || product?.name || 'Unnamed Product',
          qty: line.qty,
          price: line.price_unit,
          subtotal: line.price_subtotal,
          discount: line.discount || 0,
        }
      }),
      tax_amount: order.amount_tax || order.get_total_tax?.(),
    }

    try {
      const result = await this.orm.call('sale.order', 'create_saleorder_from_pos', [
        orderDetails,
      ])
      if (!result) {
        this.dialogService.add(AlertDialog, {
          title: _t('Error'),
          body: _t('Backend did not return a valid response.'),
        })
        return
      }

      const orderId = result.id || (typeof result === 'number' ? result : null)
      const orderName = result.name || `SO${orderId}`

      this.dialog.add(ConfirmationDialog, {
        title: _t('Success'),
        body: _t(`Sale Order ${orderName} created successfully!`),
        confirmLabel: _t('Confirm Order'),
        cancelLabel: _t('Close'),
        confirm: () => {
          if (orderId) {
            this.orm.call('sale.order', 'action_confirm', [orderId])
          }
        },
      })

      this.pos.addNewOrder()
    } catch (err) {
      this.dialogService.add(AlertDialog, {
        title: _t('Error'),
        body: _t('Could not create Sale Order. Check backend logs.'),
      })
    }
  },
})
