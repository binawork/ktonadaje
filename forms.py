from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, SubmitField, BooleanField 
from wtforms import SelectMultipleField, DecimalField
from wtforms.fields.html5 import DateTimeField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL


class AddEventForm(FlaskForm):
    """Adding event form"""
    event_title = StringField("Title", [
        DataRequired(message="This field is required."),
        Length(min=3, message="Your title is too short."),
    ])
    host_name = StringField("Host full name", [
        DataRequired(message="This field is required."),
        Length(min=3, message="Your name is too short."),
    ])
    event_link = URLField("Link", [
        DataRequired(message="This field is required."),
        URL(message="Not valid url adress."),
    ])
    start_datetime = DateTimeField("Start date-time", [
        Optional(),
    ], format='%d-%m-%Y %H:%M'
    )
    estimated_duration = DecimalField("Duration", [
        Optional(),
    ])
    event_categories = SelectMultipleField("Categories", [
        Optional(),
    ], coerce=int,
    )
    event_description = TextField("Event description", [
        Optional(),
    ])
    # agreement_checkbox = BooleanField("Accept agreement")
    # recaptcha = RecaptchaField()
    submit = SubmitField("Dodaj")


# TODO: Add class AddRegistrationForm

# TODO: Add class AddLoginForm (inherit from class AddRegistrationForm)
