import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

import config
from forms import EventForm


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *


@app.route('/')
@app.route('/events')
def index():
    events = Event.query.all()
    return render_template(
                        'events_table.html', 
                        events=events
                        )


@app.route('/add-event', methods = ('GET', 'POST'))
def add_event():
    form = EventForm()
    choices = [
        (category.title, category.title) for category in Category.query.order_by("title")
    ]
    print(choices)
    form.event_category.choices = choices
    if form.validate_on_submit():
        return redirect(url_for('index'))
    
    return render_template('events/add_event.html', form=form)





@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        request.form['']
        return redirect('index')
    else:
        return render_template('users/register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('index')
    else:
        return render_template('users/login.html')


@app.route('/services')
def services_catalog():
    services = "usługi"
    return render_template('services_catalog.html', services=services)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/how-to-streaming')
def howto_streaming():
    return render_template('howto_streaming.html')


if __name__ == '__main__':
    app.run()
