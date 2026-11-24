# -*- coding: utf-8 -*-
{
    "name": "POS Invoice Auto Print",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "author": "Fathia BEN MOHAMED",
    "summary": "Configure automatic invoice printing in Point of Sale",
    "description": """
    POS Invoice Auto Print
    ======================
    This module adds an option to enable or disable automatic invoice printing.
    Features:
    ---------
    - Enable automatic invoice printing.
    - Disable automatic invoice printing when not needed.
    """,
    "depends": ["base", "point_of_sale"],
    "data": [
        "views/res_config_settings.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_invoice_auto_print/static/src/**/*",
        ],
    },
    "application": False,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
