# -*- coding: utf-8 -*-
{
    "name": "Account Payment Methods",
    "version": "19.0.2.0.0",
    "summary": "Add account payment methods",
    "category": "Accounting",
    "author": "Fathia BEN MOHAMED",
    "depends": ["account"],
    "data": [
        "data/account.payment.method.csv",
        "views/account_payment_views.xml",
        "views/account_payment_method_views.xml",
        "views/account_payment_register_views.xml",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
