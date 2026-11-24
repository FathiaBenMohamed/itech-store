# -*- coding: utf-8 -*-

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = "pos.config"

    invoice_auto_print = fields.Boolean(
        string="Invoice Auto Print",
        help="Enable this option to automatically print the invoice.",
    )
