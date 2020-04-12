from flask import Flask, render_template
import data_manager
app = Flask(__name__)


@app.route('/')
def index():
    services = data_manager.get_all()
    return render_template('Table.html', services=services)

@app.route('/trenerzy_osobisci')
def trenerzy_osobisci():
    database_connection.connection_handler()
    return render_template('uslugi.html', uslugi=uslugi)



if __name__ == '__main__':
    app.run()
