# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_tax_stamp = fields.Boolean(
        string="Timbre Fiscal", default=False, copy=False, tracking=True
    )
