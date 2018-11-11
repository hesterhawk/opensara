from flask import Blueprint, current_app, render_template, flash, redirect, url_for
from flask_login import current_user
from datetime import datetime

from .forms.create import CreateCustomerForm

customer = Blueprint('customer', __name__, template_folder="views")

from app import db
from app.models.project import Project
from app.models.customer import Customer

@customer.route('/customers/<int:project_id>', methods=['GET', 'POST'])
def all(project_id: int):
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    project = Project.query.get(project_id)

    form = CreateCustomerForm()

    if form.validate_on_submit():
        pass
        """
        project = Project(state=1, created_date=datetime.now(), fullname=form.fullname.data)
        project.set_random_token()
        db.session.add(project)
        db.session.commit()
        """

        flash("Project created successfully!")
        return redirect(url_for('project.all'))   

    return render_template('customers.html', project=project, form=form)