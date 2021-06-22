# coding: utf-8
# © 2019 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'FP - Ubicaciones de pick en almacén',
    'description': '' ,
    'version': '8.0.2',
    'author': 'Felipe Arcos',
    'category': 'General',
    'depends': [
        'sale'
    ],
    'data': [
        'views/stock_picking.xml',
        'views/pick_location.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
