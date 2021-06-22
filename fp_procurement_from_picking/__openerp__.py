# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Abastecimiento desde albarán',
    'description': '' ,
    'version': '8.0.5',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product', 'purchase',
    ],
    'data': [
        'views/stock_picking.xml',
        'views/stock_move.xml',
        'views/procurement.xml',
        'views/purchase_order.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
