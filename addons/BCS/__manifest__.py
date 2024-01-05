{
    'name': 'BCS Clients',
    'version': '1.0.0',
    'author': 'Mhamed',
    'category': 'Clients',
    'sequence': -100,
    'summary': 'manage clients',
    'description': """manage clients """,
    'depends': ['base', 'web'],
    'qweb': ['static/src/xml/*.xml'],
    'data': [
  
        'security/ir.model.access.csv',

        'report/user_card.xml',
        'report/report.xml',
        'views/menu.xml',
        'views/clients_view.xml',
        'views/farms_view.xml',
        'views/zones_view.xml',
        'views/sensors_view.xml',
        'views/data_view.xml',
        'data/res.data.csv'
    ],
    'assets': {
        'web.assets_backend': [
            #  'BCS/static/bg.css',  # Include your CSS file
        ],
    },
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
