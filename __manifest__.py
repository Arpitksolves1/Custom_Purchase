# -*- coding: utf-8 -*-


{
    'name': 'Custom Purchase',
    'version': '1.0.0',
    'category': 'Custom Purchase',
    'sequence': 1,
    'summary': 'Custom Purchase Line',
    'description': "All the details of purchasing details are present in this model",
    'depends': ['base', 'purchase', 'account'],
    'data': [
        "security/ir.model.access.csv",
        "wizard/wizard_view.xml",
        "views/custom_purchase_order_views.xml",
        # "views/menu_view.xml",
        'views/vendor_bill_view.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
}
