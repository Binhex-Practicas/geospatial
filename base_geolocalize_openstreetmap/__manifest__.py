# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Base Geolocalize Openstreetmap',
    'summary': """
        Open street map API call to geolocalize an address""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/geospatial',
    'depends': [
        'base_geoengine',
    ],
    'external_dependencies': {
        'python': [
            'requests'
        ],
    },
}
