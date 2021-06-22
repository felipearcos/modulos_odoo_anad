# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Etiquetas pegatinas producto',
    'version': '8.0.4',
    'category': 'Reports',
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'installable': True,
    'depends' : [
        'stock', 
        'report',
    ],
    'data': [
        'views/product_product_label_view.xml',
        'report/label.xml',
    ],
}
