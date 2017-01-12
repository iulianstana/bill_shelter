from datetime import datetime

from flask import render_template
from pdfkit import from_string

from app import app
from config import pdf_options


def get_notice_data(bath_old, bath_new, kitchen_old, kitchen_new, water_type):
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
        'type': water_type.center(15, " "),
        "completed_date": current_date.strftime("%Y-%m-%d").center(20, " "),
    }
    return result


@app.route('/', methods=['GET'])
def __index__():
    cold_notice = get_notice_data(1139.472, 1145.128, 226.892, 227.515, 'APA RECE')
    hot_notice = get_notice_data(632.34, 635.287, 351.359, 352.355, 'APA CALDA')
    render_obj = render_template('water_notice.html', notices=[cold_notice, hot_notice])
    #from_string(render_obj, "water_shelter/test.pdf", options=pdf_options)
    return render_obj

