from datetime import datetime

from flask import render_template
from pdfkit import from_string

from app import app
from config import pdf_options


def get_notice_data(bath_old, bath_new, kitchen_old, kitchen_new):
    time_frame = ['Ianuarie', 'Februarie']
    notice_number = '10'
    current_date = datetime.now()
    result = {
        'nr_apartment': 79,
        'notice_number': notice_number.center(6, " "),
        'start_time': time_frame[0].center(30, " "),
        'end_time': time_frame[1].center(30, " "),
        'bath_old': bath_old,
        'bath_new': bath_new,
        'kitchen_old': kitchen_old,
        'kitchen_new': kitchen_new,
        'type': 'Rece'.center(15, " "),
        "completed_date": current_date.strftime("%Y-%m-%d").center(20, " "),
    }
    cold_notice = render_template('water_notice.html', result=result)
    return cold_notice


@app.route('/', methods=['GET'])
def __index__():
    cold_notice = get_notice_data(1139.472, 1145.128, 226.892, 227.515)
    from_string(cold_notice, "water_shelter/test.pdf", options=pdf_options)
    return cold_notice

