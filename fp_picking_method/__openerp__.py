# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Adaptación al nuevo método de traspaso de albaranes',
    'description': 'Nuevo campo en las líneas del pedido de compra para indicar el motivo del abastecimiento, nuevo informe de albarán' ,
    'version': '8.0.1',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'product', 'purchase',
    ],
    'data': [
        'data/fp_picking_paper.xml',
        'views/purchase_order.xml',
        'views/stock_picking.xml',
        'report/fp_picking_template.xml',
        'report/fp_report.xml',
        'report/fp_template.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
