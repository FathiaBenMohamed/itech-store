import { ReceiptHeader } from '@point_of_sale/app/screens/receipt_screen/receipt/receipt_header/receipt_header'
import { usePos } from '@point_of_sale/app/hooks/pos_hook'
import { patch } from '@web/core/utils/patch'

patch(ReceiptHeader.prototype, {
  setup() {
    super.setup(...arguments)
    this.pos = usePos()
  },
  get partnerInfos() {
    return this.pos.getPartnerCredit(this.order.getPartner())
  },
})
