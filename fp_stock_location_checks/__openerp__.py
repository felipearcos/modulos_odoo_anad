# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'FP - Checkbox especiales de ubicaciones de almacen',
    'summary': 'Permite marcar si un producto tiene doble ubicacion, es de venta prioritaria o solo de exposicion',
    'version': '8.0.3',
    'category': 'Inventory',
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'product',
        'stock','sale_stock','fp_location_by_product'
    ],
    'data': [
        'views/product.xml',
        'views/fp_stock_location_checks.xml',	
        ],
    'css' : ['static/src/css/fp_stock_location_checks.css'],
}
