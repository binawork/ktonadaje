from flask import Flask, render_template, url_for, request
import data_manager
app = Flask(__name__)


@app.route('/')
def index():
    services = data_manager.get_all()
    return render_template('Table.html', services=services)

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
def trenerzy_osobisci():
    database_connection.connection_handler()
    return render_template('uslugi.html', uslugi=uslugi)



if __name__ == '__main__':
    app.run()
