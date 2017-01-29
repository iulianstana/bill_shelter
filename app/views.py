from datetime import datetime

from flask import render_template, redirect, url_for, request, jsonify
from sqlalchemy import desc
from pdfkit import from_string

from app import app, db
from config import pdf_options

from models import MonthNotice
from momentjs import convert_datetime_to_lang_month


def get_notice_data(old_month, new_month):
    notice_number = '10'
    current_date = datetime.now()
    result = {
        'nr_apartment': 79,
        'notice_number': notice_number.center(6, " "),
        'start_time': convert_datetime_to_lang_month(old_month.datetime).center(30, " "),
        'end_time': convert_datetime_to_lang_month(new_month.datetime).center(30, " "),
        'bath_old': old_month.bath_index,
        'bath_new': new_month.bath_index,
        'kitchen_old': old_month.kitchen_index,
        'kitchen_new': new_month.kitchen_index,
        'type': old_month.type.center(15, " "),
        "completed_date": current_date.strftime("%Y-%m-%d").center(20, " "),
    }
    return result


@app.route('/save_pdf', methods=['GET', 'POST'])
def save_pdf():
    old_month = MonthNotice.query.get(1)
    new_month = MonthNotice.query.get(2)
    cold_notice = get_notice_data(old_month.cold_notice, new_month.cold_notice)
    hot_notice = get_notice_data(old_month.hot_notice, new_month.hot_notice)
    render_obj = render_template('water_notice.html', notices=[cold_notice, hot_notice])
    from_string(render_obj, "water_shelter/test.pdf", options=pdf_options)
    return redirect(url_for('demo_notice'))


@app.route('/', methods=['GET'])
def index():
    month_notice = MonthNotice.query.order_by(desc(MonthNotice.datetime)).limit(12).all()
    return render_template('index.html', month_notice=month_notice)


@app.route('/demo_notice', methods=['POST'])
def demo_notice():
    old_month = MonthNotice.query.get(int(request.form['old_month']))
    new_month = MonthNotice.query.get(int(request.form['new_month']))
    cold_notice = get_notice_data(old_month.cold_notice, new_month.cold_notice)
    hot_notice = get_notice_data(old_month.hot_notice, new_month.hot_notice)
    render_obj = render_template('water_notice.html', notices=[cold_notice, hot_notice])
    return jsonify({'innerhtml': render_obj})
