# -*- coding: utf-8 -*-
# © 2018 Felipe Arcos (<felipe@florprohibida.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'FP - Saldo de cuentas contando la apertura',
    'version': '8.0.2',
    'category': 'account',
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'depends': [
        'account','sale'
    ],
    'data' : [
        'views/res_partner.xml',
        'views/account_account.xml'
    ],
    'installable': True,
}
