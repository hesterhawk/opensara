from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

from .config.app import Config

app = Flask(__name__, template_folder='resources/views', static_folder='resources/static')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

if True != Config.DEBUG_APP:
    from app import errors

from .opensara.auth.controllers import auth
from .opensara.main.controllers import main
from .opensara.project.controllers import project
from .opensara.customer.controllers import customer

"""
    [BUG] blueprint template_folder: https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
"""

app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(project)
app.register_blueprint(customer)

# app.url_map