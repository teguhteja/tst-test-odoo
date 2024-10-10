# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "POS Customizations",
    "author": "IB Teguh TM",
    'maintainer': 'teguh.teja@gmail.com',
    "website": "https://teguhteja.id",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "installable": True,
    'category': 'POS',
    'summary': 'Customizations for POS module',
    'description': """
        Disable Price and Discount buttons in POS.
    """,
    'depends': ['base','point_of_sale'],
    'data': [
         'views/assets.xml',
        #  'views/pos_payment_screen.xml',
    ],
    'installable': True,
    'application': False,
}
