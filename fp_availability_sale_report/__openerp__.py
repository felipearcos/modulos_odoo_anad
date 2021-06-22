# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'FP - Presupuesto para comprobar disponibilidad',
    'version': '8.0.1',
    'category': 'Reports',
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'sale',
        'stock',
        'account' 
    ],
    'data': [
        'data/fp_sale_paper.xml',
        'report/fp_sale_template.xml',
        'report/fp_report.xml',
        'report/fp_template.xml',
    ],
}
