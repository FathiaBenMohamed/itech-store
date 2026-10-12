# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    price_unit_ht = fields.Float(
        string="PU HT",
        compute="_compute_price_unit_ht",
        min_display_digits="Product Price",
    )
    price_unit_ht_net = fields.Float(
        string="PU HT net",
        compute="_compute_price_unit_ht_net",
        min_display_digits="Product Price",
    )

    @api.depends("price_subtotal", "quantity")
    @api.depends_context("company")
    def _compute_price_unit_ht_net(self):
        for record in self:
            price_unit_ht_net = 0.0
            if record.quantity:
                price_unit_ht_net = record.price_subtotal / record.quantity
            record.price_unit_ht_net = price_unit_ht_net

    @api.depends("tax_ids", "price_unit")
    @api.depends_context("company")
    def _compute_price_unit_ht(self):
        for record in self:
            record.price_unit_ht = record._construct_price_unit_ht(record.price_unit)

    def _construct_price_unit_ht(self, price):
        currency = self.currency_id
        res = self.tax_ids._filter_taxes_by_company(self.env.company).compute_all(
            price, product=self.product_id, partner=self.env["res.partner"]
        )
        amount = 0.0
        included = res["total_included"]
        if currency.compare_amounts(included, price):
            amount = included
        excluded = res["total_excluded"]
        if currency.compare_amounts(excluded, price):
            amount = excluded
        return amount
