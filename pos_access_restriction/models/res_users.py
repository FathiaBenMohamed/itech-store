# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    """Adds the list of Points of Sale a user is allowed to access.

    Security note: the actual restriction is NOT enforced by this field
    alone. It is enforced by the ir.rule records defined in
    security/pos_security.xml (applied on pos.config, pos.session,
    pos.order, pos.payment) and reinforced by explicit Python checks in
    pos_config.py / pos_session.py / pos_order.py. This field is only the
    data source used by those rules.
    """

    _inherit = "res.users"

    allowed_pos_ids = fields.Many2many(
        comodel_name="pos.config",
        relation="res_users_pos_config_rel",
        column1="user_id",
        column2="pos_config_id",
        string="Allowed POS",
        help="Points of Sale this user is allowed to open and use. "
        "If left empty, the user cannot access ANY Point of Sale "
        "(unless they belong to the POS Administrator/Manager group).",
    )
