from flask import session
from . import admin

@admin.route('/')
def index():
    return "مدیریت وبلاگ!"


@admin.route('/login/')
def login():
    session['name'] = 'Majid'
    print(session)
    return "admin login!!"