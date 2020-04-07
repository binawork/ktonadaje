from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Layout.html')

@app.route('/trenerzy_osobisci')
def trenerzy_osobisci():
    database_connection.connection_handler()
    return render_template('uslugi.html', uslugi=uslugi)



if __name__ == '__main__':
    app.run()
