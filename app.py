from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import config


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *


@app.route('/')
def index():
    events = Event.query.all()
    return render_template('Table.html',
                           events=events)


@app.route('/dodaj_wydarzenie', methods = ['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        request.form['']
        return redirect('index')
    else:
        return render_template('event_questionare.html')


@app.route('/zarejestruj', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        request.form['']
        return redirect('index')
    else:
        return render_template('register.html')


@app.route('/zaloguj', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('index')
    else:
        return render_template('login.html')


@app.route('/trenerzy_osobisci')
def services_catalog():
    services = "usługi"
    return render_template('services_catalog.html', services=services)


@app.route('/o_nas')
def about_us():
    return render_template('about_us.html')


@app.route('/jak_streamowac')
def how_to_stream():
    return render_template('how_to_stream.html')


if __name__ == '__main__':
    app.run()
