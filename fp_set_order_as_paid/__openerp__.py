# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Marcar pedido como pagado o no',
    'description': '' ,
    'version': '8.0.1',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'sale', 'stock',
    ],
    'data': [
        'views/sale_order.xml',
        'views/stock_picking.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
