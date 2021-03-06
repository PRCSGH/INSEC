# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    'name': 'Security for Menu (Enterprise)',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'summary': """
        This module is used to hide menu for user or groups.
    """,
    'description': """
        This module is used to hide menu for user or groups.
    """,
    'price': 25.00,
    'currency': 'EUR',
    'author': "Acespritech Solutions Pvt. Ltd.",
    'website': "http://www.acespritech.com",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_view.xml'
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
