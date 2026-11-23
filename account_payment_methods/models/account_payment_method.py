from odoo import api, models


class AccountPaymentMethod(models.Model):
    _inherit = "account.payment.method"

    @api.model
    def _get_payment_method_information(self):
        res = super(AccountPaymentMethod, self)._get_payment_method_information()
        payment_methods = ("check", "cash", "banknote", "transfer", "tpe", "rs")
        for payment_method in payment_methods:
            res[payment_method] = {
                "mode": "multi",
                "domain": [("type", "in", ("bank", "cash"))],
            }
        return res
