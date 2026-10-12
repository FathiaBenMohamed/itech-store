# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    total_ht_brut = fields.Monetary(
        string="Total Before Discount",
        compute="_compute_total_discount",
        store=True,
        help="Sum of all line totals before applying discounts",
        currency_field="currency_id",
    )

    total_discount = fields.Monetary(
        string="Total Discount",
        compute="_compute_total_discount",
        store=True,
        help="Sum of all discounts in the invoice lines",
        currency_field="currency_id",
    )

    tva_without_stamp = fields.Monetary(
        string="TVA sans TF",
        compute="_compute_tva_without_stamp",
        store=True,
        currency_field="currency_id",
    )

    @api.depends("amount_tax", "amount_stamp_tax")
    def _compute_tva_without_stamp(self):
        for record in self:
            record.tva_without_stamp = record.amount_tax - record.amount_stamp_tax

    @api.depends(
        "invoice_line_ids.price_subtotal",
        "invoice_line_ids.price_unit",
        "invoice_line_ids.quantity",
        "invoice_line_ids.discount",
    )
    def _compute_total_discount(self):
        for invoice in self:
            total_discount = 0.0
            total_ht_brut = 0.0
            if invoice.move_type in (
                "out_invoice",
                "out_refund",
                "in_invoice",
                "in_refund",
            ):
                for line in invoice.invoice_line_ids:
                    if (
                        line.display_type
                        in ("line_section", "line_subsection", "line_note")
                        or line.is_tax_stamp
                    ):
                        continue
                    # Calculate the price before discount for each line
                    price_ht = line.quantity * line.price_unit_ht
                    total_ht_brut += price_ht
                    # Calculate the discount amount per line
                    discount_amount = price_ht * (line.discount / 100.0)
                    total_discount += discount_amount
            invoice.total_ht_brut = total_ht_brut
            invoice.total_discount = total_discount

    def _get_name_invoice_report(self):
        self.ensure_one()
        if self.company_id.account_fiscal_country_id.code == "TN":
            return "itech_reports.itech_report_invoice_document"
        return super()._get_name_invoice_report()
