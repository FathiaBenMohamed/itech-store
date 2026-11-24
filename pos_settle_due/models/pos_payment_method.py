# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    is_customer_credit = fields.Boolean(
        string="Customer Credit",
        default=False,
        help="Identify this payment method as a customer account payment method.",
    )

    @api.model
    def _load_pos_data_fields(self, config):
        result = super()._load_pos_data_fields(config)
        result += ["is_customer_credit"]
        return result
