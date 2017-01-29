from datetime import datetime

from jinja2 import Markup

from config import month_list


class momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, format):
        return Markup("<script>\ndocument.write(moment(\"%s\").%s);\n</script>" %
                      (self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), format))
    
    def format(self, fmt):
        return self.render("format(\"%s\")" % fmt)

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")


def convert_datetime_to_lang_month(month_time):
    return month_list[month_time.month - 1]