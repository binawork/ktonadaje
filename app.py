import os
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask import (
                    Flask,
                    render_template,
                    url_for,
                    request,
                    redirect,
                    make_response,
                    flash
)
import config
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from forms import AddEventForm, RegistrationForm
from models import *



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SECRET_KEY'] = os.urandom(32)
db = SQLAlchemy(app)
moment = Moment(app)
bcrypt = Bcrypt(app)


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
    if request.method == 'POST':
        if form.validate():
            new_event = Event(
                title = form.event_title.data,
                host_name = form.host_name.data,
                url = form.event_link.data,
                categories = Category.query.filter(
                    Category.id.in_(form.event_categories.data)).all(),
                planned_start = form.start_datetime.data,
                estimated_duration = form.estimated_duration.data,
                description = form.event_description.data,
            )
            # Add Event to database
            db.session.add(new_event)
            db.session.commit()
            return redirect(url_for('index'))
        return redirect(url_for('add_event'))
    # GET: Serve add-event page
    return render_template('events/add_event_wtform_tut.html',
                            title='KtoNadaje',
                            form=form)


@app.route('/edit-event/<int:id>', methods=('GET', 'POST', 'DELETE'))
def edit_event(id: int):
    """
    may be helpful: 
    https://stackoverflow.com/questions/9885693/how-i-do-to-update-data-on-\
        many-to-many-with-wtforms-and-sqlalchemy
    """
    pass


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data
                        )
            try:
                db.session.add(user)
                db.session.commit()
                flash('Registration succesfull')
                return redirect(url_for('index'))
            except IntegrityError:
                flash('Registration failed')
                return redirect(url_for('register'))
        else:
            flash('Registration failed')
            return redirect(url_for('register'))
    return render_template('users/register.html', form=form)



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
