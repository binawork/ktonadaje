import os
from flask_sqlalchemy import SQLAlchemy
from flask import (
                    Flask, 
                    render_template, 
                    url_for, 
                    request, 
                    redirect, 
                    make_response,
)

import config
from forms import EventForm


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)

from models import *


@app.route('/')
@app.route('/home')
@app.route('/events')
def index():
    events = Event.query.all()
    return render_template('events_table.html',
                            title='KtoNadaje',
                            events=events)


@app.route('/add-event', methods=('GET', 'POST'))
def add_event():
    """Adding event form"""
    form = EventForm()
    print("form.errors", form.errors)
    # POST: Add event
    if request.method == "POST":
        print(form.event_categories.data)
        if form.validate_on_submit():
            # Get form fields
            title = form.event_title.data
            host_name = form.host_name.data
            url = form.event_link.data
            categories = form.event_categories.data
            new_event = Event(
                                title=title, 
                                host_name=host_name, 
                                url=url, 
                                categories=categories
            )
            # Add to database
            print(
                    new_event.title, "||", 
                    new_event.host_name, "\n", 
                    new_event.url, "\n",
                    new_event.categories,
            )
            # db.session.add(new_event)
            # db.session.commit()
            return redirect(url_for('success'))
    # GET: Serve add-event page
    choices = [
        (category.title, 
        category.title) for category in Category.query.order_by("title")
    ]
    form.event_categories.choices = choices
    return render_template('events/add_event_wtform_tut.html',
                            title='KtoNadaje',
                            form=form)


@app.route('/success', methods=('GET', 'POST'))
def success():
    query = []
    for event in db.session.query(Event):
        query.append(event)
    return render_template('success_wtform_tut.html',
                            title='KtoNadaje',
                            query=query)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        request.form['']
        return redirect('index')
    else:
        return render_template('users/register.html',
                                title='KtoNadaje',)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('index')
    else:
        return render_template('users/login.html',
                                title='KtoNadaje',)


@app.route('/services')
def services_catalog():
    services = "usługi"
    return render_template('services_catalog.html',
                            title='KtoNadaje',
                            services=services)


@app.route('/about')
def about():
    return render_template('about.html',
                            title='KtoNadaje',)


@app.route('/how-to-streaming')
def howto_streaming():
    return render_template('howto_streaming.html',
                            title='KtoNadaje',)


@app.route("/api/v2/test_response")
def events():
    headers = {"Content-Type": "application/json"}
    response = make_response('Test worked!', 200)
    response.headers = headers
    return response


if __name__ == '__main__':
    app.run()
