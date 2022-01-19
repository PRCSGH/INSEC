# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt. Ltd. See LICENSE file for full copyright and licensing details.
{
    'name': 'Attendance Approval Workflow',
    'version': '2.1.2',
    'price': 9.0,
    'depends': [
        'hr_attendance',
    ],
    'currency': 'EUR',
    'license': 'Other proprietary',
    'category': 'Human Resources/Attendances',
    'summary':  """This app allows your user to approve workflow on Attendance.""",
    'description': """
This app allows your user to approve reject workflow on Attendance.
    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.probuse.com',
    'images': ['static/description/image1.png'],
    'live_test_url': 'https://youtu.be/YQ2rQYJw0iQ',
    'data': [
        'security/ir.model.access.csv',
        'wizard/hr_attendance_refuse_wizard_view.xml',
        'wizard/hr_attendance_approve_wizard_view.xml',
        'views/hr_attendance_view.xml',
    ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
