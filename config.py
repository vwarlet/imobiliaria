from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = "login_bp.login"
