# -*- coding: utf-8 -*-
# 2018 Felipe Arcos <felipe@florprohibida.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'FP - Cliente en TPV',
    'summary': 'Permite seleccionar un cliente por defecto en el TPV',
    'version': '8.0.1',
    'category': 'General',
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'views/pos_config.xml']
}
