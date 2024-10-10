# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Material Registration ",
    "author": "IB Teguh TM",
    'maintainer': 'teguh.teja@gmail.com',
    "website": "https://teguhteja.id",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "installable": True,
    'category': 'Inventory',
    'summary': 'Module for registering materials to be sold.',
    'description': """
        This module allows users to register materials that will be sold.
        It includes fields for Material Code, Material Name, Material Type,
        Material Buy Price, and Related Supplier. Users can view, filter,
        update, and delete materials.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
