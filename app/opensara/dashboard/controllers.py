from flask import Blueprint, current_app, render_template, flash, redirect, url_for
from flask_login import current_user
from datetime import datetime

dashboard = Blueprint('dashboard', __name__, template_folder="views")

from app import db
from app.models.project import Project

# TODO
@dashboard.route('/dashboard', methods=['GET'])
def main():

    return render_template(
        'dashboard.html', 
        menu='_dashboard',
        project=current_user.projects[0]
    )    

