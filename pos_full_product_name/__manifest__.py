# -*- coding: utf-8 -*-

{
    "name": "POS Full Product Name",
    "summary": "Display full product name in the POS module.",
    "description": "This module helps the user to display"
    " full product name in the POS module.",
    "author": "Fathia BEN MOHAMED",
    "category": "Point of Sale",
    "version": "19.0.1.0.0",
    "depends": ["point_of_sale"],
    "data": [],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_full_product_name/static/src/**/*",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
