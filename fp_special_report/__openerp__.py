# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Presupuesto y factura especiales',
    'version': '8.1',
    'category': 'Reports',
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'account'
        
    ],
    'data': [
        'data/fp_paper.xml',
        'report/fp_invoice_template.xml',
        'report/fp_report.xml',
        'report/fp_template.xml',
        'report/fp_quotation_template.xml',
    ],
}
