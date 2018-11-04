from flask import Blueprint, current_app, render_template, flash, redirect, url_for
from flask_login import current_user
from datetime import datetime

from .forms.create_project import CreateProjectForm
from .forms.update_project import UpdateProjectForm

project = Blueprint('project', __name__, template_folder="views")

from app import db
from app.models.project import Project

@project.route('/projects', methods=['GET'])
def all():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('all.html')    

@project.route('/project/create', methods=['GET', 'POST'])
def create():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    form = CreateProjectForm()

    if form.validate_on_submit():
        project = Project(state=1, created_date=datetime.now(), fullname=form.fullname.data)
        project.set_random_token()
        db.session.add(project)
        db.session.commit()

        flash("Project created successfully!")
        return redirect(url_for('project.all'))    

    return render_template('create.html', form=form)