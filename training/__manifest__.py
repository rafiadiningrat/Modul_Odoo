# -*- coding: utf-8 -*-
{
    'name': "training odoo",

    'summary': """
        Latihan Modul Baru Odoo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Aptavis",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/employee.xml',
        'views/schedule.xml',
        'views/route.xml',
        'views/bus.xml',
        'views/passanger.xml',
        'views/menu_items.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
