from datetime import datetime

from flask import render_template, redirect, url_for, request, jsonify
from pdfkit import from_string

from app import app, db
from config import pdf_options

from models import MonthNotice


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


@app.route('/save_pdf', methods=['GET', 'POST'])
def save_pdf():
    cold_notice = get_notice_data(1139.472, 1145.128, 226.892, 227.515, 'APA RECE')
    hot_notice = get_notice_data(632.34, 635.287, 351.359, 352.355, 'APA CALDA')
    render_obj = render_template('water_notice.html', notices=[cold_notice, hot_notice])
    from_string(render_obj, "water_shelter/test.pdf", options=pdf_options)
    return redirect(url_for('demo_notice'))


@app.route('/', methods=['GET'])
def index():
    month_notice = MonthNotice.query.all()
    print month_notice
    return render_template('index.html', month_notice=month_notice)


@app.route('/demo_notice', methods=['POST'])
def demo_notice():
    old_month = MonthNotice.query.get(int(request.form['old_month']))
    new_month = MonthNotice.query.get(int(request.form['new_month']))
    cold_notice = get_notice_data(1139.472,
                                  1145.128,
                                  226.892,
                                  227.515,
                                  'APA RECE')
    hot_notice = get_notice_data(632.34,
                                 635.287,
                                 351.359,
                                 352.355,
                                 'APA CALDA')
    render_obj = render_template('water_notice.html', notices=[cold_notice, hot_notice])
    return jsonify({'innerhtml': render_obj})
