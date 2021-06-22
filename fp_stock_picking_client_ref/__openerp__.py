# coding: utf-8
# © 2018 Felipe Arcos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Referencia de pedido en albaran',
    'description': 'Enlaza la referencia del pedido de venta con el albaran, para facilitar la busqueda de los pedidos de la web' ,
    'version': '8.0.3',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product','sale', 'sale_stock'
    ],
    'data': [
        'views/stock_picking_view.xml','views/stock_picking_report.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
}
