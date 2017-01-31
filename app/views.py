import os
from datetime import datetime

from flask import render_template, redirect, url_for, request, jsonify
from sqlalchemy import desc
from pdfkit import from_string

from app import app, db
from config import pdf_options, indent_const, ap_number

from .models import MonthNotice, Notice
from .momentjs import convert_datetime_to_lang_month, default_notice
from .forms import NoticeForm


def get_notice_data(old_month, new_month):
    notice_number = str(default_notice(new_month.datetime))
    current_date = datetime.now()
    result = {
        'nr_apartment': ap_number,
        'notice_number': notice_number.center(indent_const['notice_number'], " "),
        'start_time': convert_datetime_to_lang_month(old_month.datetime).center(indent_const['time_frame'], " "),
        'end_time': convert_datetime_to_lang_month(new_month.datetime).center(indent_const['time_frame'], " "),
        'bath_old': old_month.bath_index,
        'bath_new': new_month.bath_index,
        'kitchen_old': old_month.kitchen_index,
        'kitchen_new': new_month.kitchen_index,
        'type': old_month.type.center(indent_const['type'], " "),
        "completed_date": current_date.strftime("%Y-%m-%d").center(indent_const['complete_date'], " "),
    }
    return result


@app.route('/save_pdf', methods=['GET', 'POST'])
def save_pdf():
    old_month = MonthNotice.query.get(int(request.form['old_month']))
    new_month = MonthNotice.query.get(int(request.form['new_month']))
    cold_notice = get_notice_data(old_month.cold_notice, new_month.cold_notice)
    hot_notice = get_notice_data(old_month.hot_notice, new_month.hot_notice)
    render_obj = render_template('water_notice.html', notices=[cold_notice, hot_notice])

    # save to pdf and redirect to index
    # <number>_<YEAR-MONTH>_<YEAR-MONTH>.pdf ex: 8_2016-12_2017-12.pdf
    pdf_name = "%d_%s_%s.pdf" % (default_notice(new_month.datetime),
                             old_month.datetime.strftime("%Y-%m"),
                             new_month.datetime.strftime("%Y-%m"),)
    from_string(render_obj, os.path.join("water_shelter", pdf_name), options=pdf_options)
    return redirect(url_for('index'))


@app.route('/new_water_notice', methods=['GET', 'POST'])
def new_water_notice():
    form = NoticeForm()
    if form.validate_on_submit():
        hot = Notice(type="APA CALDA",
                     bath_index=form.hot_water_bath.data,
                     kitchen_index=form.hot_water_kitchen.data,
                     datetime=form.notice_time.data)
        cold = Notice(type="APA RECE",
                      bath_index=form.cold_water_bath.data,
                      kitchen_index=form.cold_water_kitchen.data,
                      datetime=form.notice_time.data)

        month_notice = MonthNotice(cold_notice=cold,
                                   hot_notice=hot,
                                   datetime=form.notice_time.data)

        db.session.add(hot)
        db.session.add(cold)
        db.session.add(month_notice)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('new_water_notice.html', form=form)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    month_notice = MonthNotice.query.order_by(desc(MonthNotice.datetime)).limit(12).all()
    return render_template('index.html', month_notice=month_notice)


@app.route('/preview_notice', methods=['POST'])
def demo_notice():
    old_month = MonthNotice.query.get(int(request.form['old_month']))
    new_month = MonthNotice.query.get(int(request.form['new_month']))
    cold_notice = get_notice_data(old_month.cold_notice, new_month.cold_notice)
    hot_notice = get_notice_data(old_month.hot_notice, new_month.hot_notice)
    render_obj = render_template('water_notice.html', notices=[cold_notice, hot_notice])
    return jsonify({'innerhtml': render_obj})
