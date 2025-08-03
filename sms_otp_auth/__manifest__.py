# -*- coding: utf-8 -*-
# Copyright 2025 GalaxyITC
{
    'name': 'SMS OTP Auth',
    'version': '1.0.0',
    'author': "BusinessFlow Systems",
    'website': "https://www.odoo.com",
    'category': 'Extra Tools/Authentication',
    'summary': "Module for SMS-based OTP Authentication",
    'description': """
    <h2>Overview</h2>
    <p>This module adds awesome features for managing your custom workflow.</p>

    <h3>Main Features</h3>
    <ul>
        <li>Feature 1: Easy integration</li>
        <li>Feature 2: Clean interface</li>
        <li>Feature 3: Lightweight and fast</li>
    </ul>

    <h3>Usage</h3>
    <p>After installing, go to the menu and configure your options.</p>
    """,
    'depends': [
        'base', 'portal', 'auth_signup', 'mail'
    ],
    'license': 'LGPL-3',
    'price': 50.00,
    'currency': 'USD',

    'data': [
        'security/ir.model.access.csv',
        'views/sms_auth.xml',
        'views/auth.xml',
        'views/res_config_setting_views.xml',
    ],
    'images': ['static/description/logo.png'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
