# coding: utf-8
# © 2018 Felipe Arcos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Marcar si un producto está servido en albarán',
    'description': 'Permite especificar en el albarán de salida si un producto está servido y la cantidad servida' ,
    'version': '8.0.2',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product', 'stock'    ],
    'data': [
        'views/stock_move_view.xml',
        'views/stock_picking_view.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
