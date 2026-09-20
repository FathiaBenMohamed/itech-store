{
    "name": "Create Sales Order From POS",
    "version": "19.0.1.0.0",
    "category": "Sales/Point of Sale",
    "summary": "Create sale order from pos screen",
    "author": "Fathia BEN MOHAMED",
    "description": """
    """,
    "depends": ["point_of_sale", "sale_management", "web", "pos_sale", "sale"],
    "data": [
        "views/res_config_settings.xml",
        "views/sale_order_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "/pos_create_so/static/src/app/control_buttons/control_buttons.xml",
            "/pos_create_so/static/src/app/control_buttons/control_buttons.js",
            "/pos_create_so/static/src/overrides/models/pos_store.js",
        ],
    },
    "application": False,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
