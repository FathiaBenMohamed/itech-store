# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = "account.payment"

    method_payment_id = fields.Many2one(
        "payment.method", "Payment Method", required=True
    )
