# -*- coding: utf-8 -*-
{
    "name": "Tax Stamp",
    "version": "19.0.1.0.0",
    "description": "Tax Stamp",
    "summary": "Add a product as a tax stamp",
    "category": "External",
    "author": "Fathia BEN MOHAMED",
    "license": "Other proprietary",
    "depends": ["base", "product", "account"],
    "data": [
        "views/product_template.xml",
        "views/account_move_line.xml",
    ],
    "application": False,
    "auto_install": False,
    "installable": True,
    "sequence": 1,
}
