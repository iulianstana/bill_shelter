# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you will never guess'

# pdfkit options 
pdf_options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

indent_const = {
    'notice_number': 6,
    'time_frame': 75,
    'type': 15,
    'complete_date': 20,
}

ap_number = 79

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

month_list = ['Ianuarie', 'Februarie', 'Martie', 'Aprilie',
              'Mai', 'Iunie', 'Iulie', 'August',
              'Septembrie', 'Octombrie', 'Noiembrie', 'Decembrie']
first_notice_date = "2016-05"
