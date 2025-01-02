{
    "name": "Hotel Management",
    "version": "1.0",
    'description': 'A system that manages hotel.',
    'summary': 'Hotel management system for a hotel.',
    'author': 'LeePT',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        'views/menu.xml',
        "views/hotel_views.xml",
        "views/room_views.xml",
        "views/feature_views.xml",
        "views/booking_views.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
