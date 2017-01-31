from datetime import datetime

from flask_wtf import FlaskForm

from wtforms import FloatField, DateTimeField
from wtforms.validators import DataRequired


class NoticeForm(FlaskForm):
    cold_water_bath = FloatField('cold_water_bath', validators=[DataRequired()])
    cold_water_kitchen = FloatField('cold_water_kitchen', validators=[DataRequired()])
    hot_water_bath = FloatField('hot_water_bath', validators=[DataRequired()])
    hot_water_kitchen = FloatField('hot_water_kitchen', validators=[DataRequired()])
    notice_time = DateTimeField("notice_time", format="%Y-%m-%d",
                                default=datetime.today,
                                validators=[DataRequired()])
