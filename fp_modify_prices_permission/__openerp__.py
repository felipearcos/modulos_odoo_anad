# coding: utf-8
# © 2018 Felipe Arcos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Permiso para modificación de precios del pedido de venta',
    'description': '' ,
    'version': '8.0.1',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'sale', 'sale_stock'],
    'data': [
        'views/res_groups_data.xml',
        'views/sale_order.xml',
        ],
    'installable': True,
    'license': 'AGPL-3',
}
