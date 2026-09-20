{
    "name": "POS Access Restriction by User",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "author": "Fathia BEN MOHAMED",
    "summary": "Restreint l'accès aux points de vente (pos.config) selon l'utilisateur",
    "description": """
POS Access Restriction by User
===============================

Ajoute un champ Many2many ``allowed_pos_ids`` sur ``res.users`` permettant de
définir la liste des Points de Vente (``pos.config``) auxquels un
utilisateur a accès.

La restriction est appliquée :

* via des règles d'enregistrement (``ir.rule``) sur ``pos.config``,
  ``pos.session``, ``pos.order`` et ``pos.payment`` (sécurité ORM, valable
  pour le backend, le frontend POS et tout appel RPC direct) ;
* via des contrôles Python explicites sur les points d'entrée sensibles
  (ouverture de session POS, création de session, création de commande),
  en défense en profondeur.

Si le champ ``allowed_pos_ids`` d'un utilisateur est vide, celui-ci n'a accès à
AUCUN point de vente. Les utilisateurs appartenant au groupe
"Administrateur / Manager Point de Vente" ne sont pas soumis à cette
restriction.
""",
    "depends": ["point_of_sale"],
    "data": [
        "security/pos_security.xml",
        "views/res_users_views.xml",
        "views/pos_config_views.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
