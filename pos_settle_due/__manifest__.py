{
    "name": "Pos Settle Due",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Settle partner's due in the POS UI.",
    "author": "Fathia BEN MOHAMED",
    "description": """
    """,
    "depends": ["point_of_sale"],
    "data": [
        "data/pos_settle_due_data.xml",
        "security/pos_security.xml",
        "security/ir.model.access.csv",
        "views/pos_payment_method_views.xml",
        "views/pos_order_views.xml",
        "views/account_move_views.xml",
        "views/res_partner_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_settle_due/static/src/**/*",
        ],
        "web.assets_unit_tests": [
            "pos_settle_due/static/tests/unit/**/*",
        ],
    },
    "application": False,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
