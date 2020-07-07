from flask_wtf import FlaskForm, RecaptchaField
from wtforms import Form
from wtforms import StringField, TextField, SubmitField, BooleanField, PasswordField
from wtforms import SelectMultipleField, DecimalField
from wtforms.fields.html5 import DateTimeField, URLField, EmailField
from wtforms.validators import DataRequired, Length, Optional, URL, EqualTo, Email


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


class RegistrationForm(Form):
    username = StringField('Username', [
        DataRequired(message="This field is required."),
        Length(min=3, max=25, message="Username must be 3-25 characters long.")
    ])

    email = EmailField('Email Address', [
        DataRequired(message="This field is required."),
        Email(message="Invalid email address")
    ])

    password = PasswordField('New Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField('Repeat Password')

    # accept_tos = BooleanField('I accept the TOS', [DataRequired()])

    submit = SubmitField("Register")


class LoginForm(Form):
    username = StringField('Username', [
        DataRequired(message="This field is required."),
        Length(min=3, max=25, message="Username must be 3-25 characters long.")
    ])

    password = PasswordField('Password', [DataRequired(),])

    submit = SubmitField("Log in")
