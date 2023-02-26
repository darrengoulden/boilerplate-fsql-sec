# Third party imports
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    render_template_string
)
from flask_mailman import Mail
from flask_security import (
    current_user,
    auth_required,
    hash_password,
    Security,
    SQLAlchemySessionUserDatastore
)
import os
from os.path import join

# Internal imports
from app.database import db
from app.models import User, Role

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

# Load env
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(basedir, '.env')
load_dotenv(dotenv_path)

if not os.environ['FLASK_DEBUG']:
    app.config.from_object('config.ProdConfig')
else:
    app.config.from_object('config.DevConfig')

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
app.security = Security(app, user_datastore)

# Flask-Mailman
mail = Mail(app)

@app.route('/')
def index():
    #return render_template_string('Hello {{email}} !', email=current_user.email)
    return render_template('index.html')

with app.app_context():
    # Create a user to test with
    db.init_app(app)
    db.create_all()
    if not app.security.datastore.find_user(email="test@me.com"):
        app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
    db.session.commit()

if __name__ == '__main__':
    app.run()
