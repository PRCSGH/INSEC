# -*- coding: utf-8 -*-
# © 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################

{
    'name'          : "Odoo Employee Attendance Geolocation",
    'version'       : '1.0.1',
    'category'      : 'Human Resources/Attendances',
    'sequence'      : 1,
    'description'   : """Odoo Employee Attendance Geolocation module Facilitates the admin to
                        record the location of their employees at the time of check-in and
                        Check-out.
                      """,
    'summary'       : """Employee attendance Geolocation module helps you to track the location
                        of your employee. It helps you to manage the employee attendances in
                        the easiest way without any error.
                        Managing employee attendance manually is a very difficult task and
                        there is a lot of possibility of mistakes in it.
                      """,
    'website'       : 'https://store.webkul.com',
    'depends'       : ['hr_attendance', 'base_geolocalize'],
    'data'          : [
                        'security/ir.model.access.csv',
                        'views/assets.xml',
                        'views/hr_attendance_view.xml',
                        'views/res_config_settings_view.xml',
                        'wizard/employee_attendance_location_wizard_view.xml'
                      ],
    'demo'          : [],
    "application"   : True,
    "installable"   : True,
    "auto_install"  : False,
    "price"         : 59,
    "currency"      : "USD",
    'pre_init_hook' : 'pre_init_check',
    "images"        : ['static/description/Banner.png'],
    "license"       : "Other proprietary",
    'author'        : 'Webkul Software Pvt. Ltd.',
    "live_test_url" : "http://odoodemo.webkul.com/?module=employee_attendance_geolocations",
}
