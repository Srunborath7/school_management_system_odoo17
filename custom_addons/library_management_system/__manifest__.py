{
    'name': 'Library Management System',
    "author": "RMA",
    "license": "LGPL-3",
    'version': '17.0.1.1',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',

        'views/student_views.xml',
        'views/book_views.xml',
        'views/category_views.xml',
        'views/borrow_views.xml',
        'views/buy_book_views.xml',
        'views/author_view.xml',
        'views/tag_book_views.xml',
        'views/hello_views.xml',
        'data/borrow_sequence.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}