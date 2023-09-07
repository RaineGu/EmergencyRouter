from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length

class CourseForm(FlaskForm):
    airways_compromised = RadioField('Airways compromised?',
                    choices=['Yes', 'No'],
                    validators=[InputRequired()])
    breathing_distress = RadioField('Is breathing in distress?',
                    choices=['Severe', 'Mild', 'None'],
                    validators=[InputRequired()])
    blood_circulation = RadioField('Blood circulation:',
                    choices=['Severe haemodynamic Compromise', 'Moderate haemodynamic Compromise', 'None'],
                    validators=[InputRequired()])
    disabilities = RadioField('Any disabilities?',
                    choices=['Yes', 'No'],
                    validators=[InputRequired()])