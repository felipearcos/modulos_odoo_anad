# -*- coding: utf-8 -*-
# © 2018 Felipe Arcos (<felipe@florprohibida.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Generador de referencias desde categoria',
    'version': '8.0.3.0.0',
    'category': 'product',
    'description': """
    Genera automaticamente referencias de producto a partir de las categorias y subcategorias de TPV.

    El objetivo es usar una referencia de 6 digitos numericos, de los que el primero represente la categoria padre 
    de TPV, los dos siguientes la primera categoria hijo y los tres ultimos la identificacion del producto.

    Es necesario asignar un digito a la categoria padre, a partir de ahi los digitos de identificacion de las subcategorias se asignaran
    de forma automatica segun la secuencia.

====================================


    """,
    'author': 'Felipe Arcos',
    'license': 'AGPL-3',
    'depends': [
        'product',
        'account',
        'point_of_sale',
    ],
    'data': [
        'data/sequence.xml',
        'views/product_view.xml',
        'views/category_view.xml',
        'wizard/update_code.xml',
    ],
    'installable': True,
}
