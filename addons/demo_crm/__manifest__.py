{
    'name': 'Demo CRM',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Demo CRM',
    'description': """
Demo CRM
    """,
    'author': 'Soy Calidad',
    'website': 'www.soycalidad.com',
    'license': 'Other proprietary',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'security/plant_nursery_groups.xml',
        'security/plant_nursery_security.xml',
        'security/plan_order_security.xml',
        'data/plant_nursery_data.xml',
        'data/mail_data.xml',
        'views/plant_order_views.xml',
        'views/res_partner_views.xml',
        'report/plant_order_views.xml',
        'report/plant_order_reports.xml',
        'report/plant_order_templates.xml',
        'wizard/make_plan_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

    'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ],
        'web.report_assets_common': [

        ],
        'web.report_assets_pdf': [

        ],
    },
}
