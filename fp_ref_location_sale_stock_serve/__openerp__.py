# coding: utf-8
# © 2018 Felipe Arcos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Calcular si un producto tiene ubicacion almacen - Marcar si un producto está servido en albaran',
    'description': 'Por un lado calcula en las líneas del pedido de venta si el producto tiene ubicación de almacén en el almacén seleccionado. Por otro permite especificar en el albarán de salida si un producto está servido y la cantidad servida' ,
    'version': '8.0.4',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product', 'stock', 'sale', 'sale_stock', 'fp_set_order_as_paid'   ],
    'data': [
        'views/stock_move_view.xml',
        'views/sale_order.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
}
