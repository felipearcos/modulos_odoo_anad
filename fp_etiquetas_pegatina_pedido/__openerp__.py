# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Etiquetas pegatinas de pedido',
    'version': '8.0.1',
    'category': 'Reports',
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'installable': True,
    'depends' : [
        'stock', 
        'report',
    ],
    'data': [
        'views/sale_label_view.xml',
        'report/label.xml',
    ],
}
