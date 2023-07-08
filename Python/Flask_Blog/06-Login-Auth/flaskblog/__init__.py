from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# setting the route where the login_manager is implemented i.e "login"
login_manager.login_view = 'login'
# setting the message category of the login_manager to a bootstrap class 'info'
login_manager.login_message_category = 'info'

from flaskblog import routes
