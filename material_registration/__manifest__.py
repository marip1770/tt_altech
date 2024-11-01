{
    'name': 'Material Registration',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Module for material registration and management (Technical Test)',
    'description': 'A custom module for registering materials and managing suppliers in Odoo 14. (Technical Test)',
    'author': 'Mochamad Ari Pratama',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/material_view.xml',
        'views/supplier_view.xml',
        'views/material_list_template.xml',
        'views/material_details_template.xml',
    ],
    'installable': True,
    'application': True,
}
