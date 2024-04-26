from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app.routes import main_bp
from app.admin.routes import admin_bp
app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(admin_bp, url_prefix="/admin")

from app import routes, models
from app.admin import admin
from app.admin import routes
