from flask import Blueprint, current_app, render_template, flash, redirect, url_for, request
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime

from .forms.create import CreateCustomerForm

customer = Blueprint('customer', __name__, template_folder="views")

from app import db
from app.models.project import Project
from app.models.customer import Customer

PER_PAGE = 10

@customer.route('/customers/<project_id>', methods=['GET', 'POST'])
def all(project_id: int):
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    project = Project.query.get(project_id)
    form = CreateCustomerForm()

    page = request.args.get(get_page_parameter(), type=int, default=1)
    customers = Customer.query.filter_by(project_id=project.id).order_by(Customer.state).paginate(page, PER_PAGE, False).items
    pagination = Pagination(per_page=PER_PAGE, page=page, total=Customer.query.count(), record_name='customers', css_framework='bootstrap4')

    if form.validate_on_submit():
        customer = Customer(
            project_id=project.id, 
            state=form.state.data, 
            instagram_login=form.instagram_login.data, 
            created_date=datetime.now()
        )

        db.session.add(customer)
        db.session.commit()

        flash("Customer created successfully!")
        return redirect(url_for('customer.all', project_id=project.id))

    return render_template(
        'customers.html', 
        project=project, 
        customers=customers,
        pagination=pagination,
        form=form
    )

@customer.route('/customer/<id>', methods=['GET', 'POST'])
def show(id: int):
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    customer = Customer.query.get(id)

    return render_template('customer.html', customer=customer)