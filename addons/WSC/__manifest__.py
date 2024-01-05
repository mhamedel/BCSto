{
    'name': 'BCS website',
    'version': '1.0.0',
    'author': 'Mhamed',
    'category': 'Clients',
    'sequence': -100,
    'summary': 'manage clients',
    'description': """manage clients """,
    'depends': [
        'base',
        'web',
        'website',
        ],
    'qweb': ['static/src/xml/*.xml'],
    'data': [

        
         'views/layouts.xml',
         'views/links.xml',

    ],
    'assets': {
            'web.assets_common': [
                #  'WSC/static/src/js/sensor_data_page.js',
              
            ],
    },
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
