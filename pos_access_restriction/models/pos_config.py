# -*- coding: utf-8 -*-
from odoo import models, fields


class PosConfig(models.Model):
    _inherit = "pos.config"

    assigned_user_ids = fields.Many2many(
        "res.users",
        string="Assigned Users",
        relation="res_users_pos_config_rel",
        column1="pos_config_id",
        column2="user_id",
        help="Users assigned to this Point of Sale.",
    )
