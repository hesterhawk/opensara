from flask import Blueprint, current_app, render_template, flash, redirect, url_for
from flask_login import current_user
from datetime import datetime

from .forms.create import CreateProjectForm
from .forms.update import UpdateProjectForm

project = Blueprint('project', __name__, template_folder="views")

from app import db
from app.models.project import Project

@project.route('/projects', methods=['GET'])
def all():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('projects.html', projects=Project.query.all())    

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

    return render_template('project_create.html', form=form)

@project.route('/project/update/<id>', methods=['GET', 'POST'])
def update(id: int):
    project = Project.query.get(id)
    form = UpdateProjectForm()

    if form.validate_on_submit():
        project.fullname=form.fullname.data        
        db.session.commit()
        
        flash("Project updated successfully!")
        return redirect(url_for('project.update', id=project.id))        

    return render_template('project_update.html', project=project, form=form)

### TODO
### Destroy project