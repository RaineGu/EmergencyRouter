from flask_wtf import FlaskForm
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import InputRequired, Length

class BusynessForm(FlaskForm):
        busyness = IntegerRangeField('Busyness of hospital', default =  5)