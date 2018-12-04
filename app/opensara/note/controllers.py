from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime
from sqlalchemy import and_

from .forms.create import CreateNoteForm
from .forms.search import SearchNotesForm

note = Blueprint('note', __name__, template_folder="views")

from app import db
from app.models.note import Note
from app.models.project import Project
from app.models.customer import Customer

PER_PAGE = 10

"""
    TODO:
        security:
        - token
        - c parameter
"""
@note.route('/notes/all/<string:project_token>', methods=['GET', 'POST'])
def all(project_token: str):

    project = Project.query.filter_by(token=project_token).first()
    customers = project.customers.all()
    select_customers = [("{}".format(c.id), c.instagram_login) for c in customers]

    filter_params = _search_filter(request, customers)

    page = request.args.get(get_page_parameter(), type=int, default=1)
    notes = Note.query.filter(and_(*filter_params)).order_by(Note.state).paginate(page, PER_PAGE, False).items
    pagination = Pagination(per_page=PER_PAGE, page=page, total=Note.query.filter(and_(*filter_params)).count(), record_name='notes', css_framework='bootstrap4')

    form_customer_id = request.args['c'] if 'c' in request.args else None

    form = CreateNoteForm(customer_id=form_customer_id)
    form.customer_id.choices = select_customers

    if form.validate_on_submit():
        note = Note(
            customer_id = form.customer_id.data,
            state=form.state.data, 
            message=form.message.data, 
            created_date=datetime.now()
        )

        db.session.add(note)
        db.session.commit()

        flash("Note created successfully!")
        return redirect(url_for('note.all', project_token=project.token))

    search_form = SearchNotesForm(request.args)
    search_form.c.choices = [('', 'customer..')] + select_customers

    return render_template(
        'notes.html',
        _menu='notes',
        form=form,
        notes=notes,
        customers=customers,
        project=project,
        pagination=pagination,
        search_form=search_form
    )

@note.route('/note/destroy/<id>', methods=['GET', 'POST'])
def destroy(id: int):

    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()
    
    flash("Note destroyed successfully!")
    return redirect(url_for('note.all', project_token=request.args['token']))

### private

def _search_filter(request, customers):

    result = []

    result.append(_construct_customers(request, customers))

    states = _construct_states(request)

    if states is not None: result.append(states)

    return result

def _construct_customers(request, customers):
    if 'c' in request.args and '' != request.args['c']:
        return Note.customer_id.in_([int(request.args['c'])])
    
    return Note.customer_id.in_([c.id for c in customers])

def _construct_states(request):
    if 's' in request.args and '' != request.args['s']:
        return Note.state.in_([request.args['s']])

    return None
