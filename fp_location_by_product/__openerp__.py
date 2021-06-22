# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'FP - Ubicaciones por producto',
    'summary': 'Permite establecer una referencia de ubicacion por cada producto',
    'version': '8.0.7',
    'category': 'Inventory',
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'product',
        'stock'
    ],
    'data': [
        'data/res_groups_data.xml',   
        'views/product.xml',
        ]
}
