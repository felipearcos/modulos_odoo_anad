# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Mensaje de aviso de stock en lineas de venta',
    'description': 'Muestra un warning si el stock disponible en el almacen/ubicacion establecida es menor a la cantidad que se quiere vender del producto' ,
    'version': '8.0.2',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product','sale', 'sale_stock', 'stock', 'warning'
    ],
    'data': [
        'views/sale_order.xml',
        'wizard/calculate_stock.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
}
