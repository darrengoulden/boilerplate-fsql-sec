# Third party imports
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    render_template
)
import os
from os.path import join

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = join(basedir, '.env')
load_dotenv(dotenv_path)

if os.environ['FLASK_ENV'] == 'prod':
    app.config.from_object('config.ProdConfig')
else:
    app.config.from_object('config.DevConfig')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
