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
from forms import AddEventForm


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
    """
    Adding Events to database through the form on the webpage.
    """
    form = AddEventForm(request.form)
    available_categories = Category.query.order_by("title")
    form.event_categories.choices = [
        (c.id, c.title) for c in available_categories
    ]
    # POST: Add event
    if form.validate_on_submit():
        new_event = Event(
            title = form.event_title.data, 
            host_name = form.host_name.data, 
            url = form.event_link.data, 
            categories = Category.query.filter(
                Category.id.in_(form.event_categories.data)).all()
        )
        # Add Event to database
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('success'))
    # GET: Serve add-event page
    return render_template('events/add_event_wtform_tut.html',
                            title='KtoNadaje',
                            form=form)


@app.route('/edit-event/<int:id>', methods=('GET', 'POST', 'DELETE'))
def edit_event(int: id):
    """
    may be helpful: 
    https://stackoverflow.com/questions/9885693/how-i-do-to-update-data-on-\
        many-to-many-with-wtforms-and-sqlalchemy
    """
    pass


@app.route('/success', methods=('GET', 'POST'))
def success():
    """
    Helper function for testing forms. 
    Displays all Events from the database after completing the form.
    """
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
