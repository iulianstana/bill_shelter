import os

from pdfkit import from_string

from config import pdf_options, notice_output
from .decorators import async


@async
def save_notice(render_string, pdf_name):
    from_string(render_string,
                os.path.join(notice_output, pdf_name),
                options=pdf_options)
