from odoo import api, models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    amount_stamp_tax = fields.Monetary(
        string="Montant TF",
        compute="_compute_amount_stamp_tax",
        store=True,
        readonly=True,
        currency_field="currency_id",
    )

    @api.depends("invoice_line_ids", "invoice_line_ids.is_tax_stamp")
    def _compute_amount_stamp_tax(self):
        for record in self:
            record.amount_stamp_tax = sum(
                record.invoice_line_ids.filtered(
                    lambda line: line.is_tax_stamp
                ).mapped(  # noqa: E501
                    "price_total"
                )
            )
