# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    pos_invoice_auto_print = fields.Boolean(related="pos_config_id.invoice_auto_print", readonly=False)
