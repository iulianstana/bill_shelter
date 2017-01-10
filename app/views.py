from flask import render_template

from app import app


@app.route('/', methods=['GET'])
def __index__():
    return render_template('water_notice.html', nr_apartament=79,
                           tip_apa="rece", numar=1, start_time=1, end_time=2)

