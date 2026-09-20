# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    method_payment_id = fields.Many2one(
        "payment.method", "Payment Method", required=True
    )

    def _create_payment_vals_from_wizard(self, batch_result):
        payment_vals = super()._create_payment_vals_from_wizard(batch_result)
        payment_vals["method_payment_id"] = self.method_payment_id.id
        return payment_vals
