from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    IntegerField,
    BooleanField,
    RadioField,
    SelectMultipleField,
    widgets,
)
from wtforms.validators import InputRequired, Length


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class CourseForm(FlaskForm):
    airways_compromised = RadioField(
        "Are airways compromised?", choices=["Yes", "No"], validators=[InputRequired()]
    )
    breathing_distress = RadioField(
        "Is breathing in distress?",
        choices=["Severe", "Moderate", "Mild", "None"],
        validators=[InputRequired()],
    )

    # Setting up blood circulation checkboxes
    string_of_bc_symptoms = [
        "Abnormal heart beat\r\nChest pain\r\nCold limbs\r\nBluish discolouration of limbs\r\nConfusion\r\nUnconsciousness\n"
    ]
    list_of_bc_symptoms = string_of_bc_symptoms[0].split("\r")
    # Create a list of value/description tuples
    bc_symptoms = [(x, x) for x in list_of_bc_symptoms]
    blood_circulation = MultiCheckboxField(
        "Compromised blood circulation - do they have:",
        choices=bc_symptoms,
    )

    # Setting up dehydration checkboxes
    string_of_dehydration_symptoms = [
        "Extreme thirst\r\nA very dry mouth\r\nA fever\r\nLittle to no urine\n"
    ]
    list_of_dehydration_symptoms = string_of_dehydration_symptoms[0].split("\r")
    # Create a list of value/description tuples
    dehydration_symptoms = [(x, x) for x in list_of_dehydration_symptoms]
    dehydration = MultiCheckboxField(
        "Dehydration - do they have:",
        choices=dehydration_symptoms,
    )

    visibly_pale = RadioField(
        "Are they visibly pale?", choices=["Yes", "No"], validators=[InputRequired()]
    )

    disabilities = RadioField(
        "Any disabilities?", choices=["Yes", "No"], validators=[InputRequired()]
    )
