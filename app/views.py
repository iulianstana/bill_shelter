from flask import render_template
from pdfkit import from_string

from app import app
from config import pdf_options


@app.route('/', methods=['GET'])
def __index__():
    cold_notice = render_template('water_notice.html', nr_apartament=79,
                                  tip_apa="rece", numar=1, start_time=1,
                                  end_time=2)
    from_string(cold_notice, "test.pdf", options=pdf_options)
    return cold_notice

