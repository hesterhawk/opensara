from flask import Blueprint, current_app, render_template, flash, redirect, url_for, request
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime

from .forms.create import CreateCustomerForm

customer = Blueprint('customer', __name__, template_folder="views")

from app import db
from app.models.project import Project
from app.models.customer import Customer
from app.middleware.user_auth import login_required

PER_PAGE = 10

@customer.route('/customers/<int:project_id>', methods=['GET', 'POST'])
def all(project_id: int):
    project = Project.query.get(project_id)
    
    page = request.args.get(get_page_parameter(), type=int, default=1)
    customers = Customer.query.filter_by(project_id=project.id).order_by(Customer.state).paginate(page, PER_PAGE, False).items
    pagination = Pagination(per_page=PER_PAGE, page=page, total=Customer.query.count(), record_name='customers', css_framework='bootstrap4')

    form = CreateCustomerForm()

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
        form=form,
        project=project, 
        customers=customers,
        pagination=pagination,
        all_customers=Customer.query.filter_by(project_id=project.id).all(),
        two_customers_count=Customer.query.filter_by(project_id=project.id,state=2).count()
    )

@customer.route('/customer/destroy/<id>', methods=['GET', 'POST'])
def destroy(id: int):

    customer = Customer.query.get(id)
    project = customer.project_id

    if 'POST' == request.method:
        db.session.delete(customer)
        db.session.commit()
        
        flash("Customer destroyed successfully!")
        return redirect(url_for('customer.all', project_id=project))

    return render_template('customer_destroy.html', customer=customer)