from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime

from .forms.create import CreateNoteForm

note = Blueprint('note', __name__, template_folder="views")

from app import db
from app.models.note import Note
from app.models.project import Project
from app.models.customer import Customer

PER_PAGE = 10

@note.route('/notes/all/<string:project_token>', methods=['GET', 'POST'])
def all(project_token: str):

    project = Project.query.filter_by(token=project_token).first()
    customers = project.customers.all()
    
    ids = [c.id for c in customers]
    form_customer_id = request.args['customer'] if 'customer' in request.args else None

    page = request.args.get(get_page_parameter(), type=int, default=1)
    notes = Note.query.filter(Note.customer_id.in_(ids)).order_by(Note.state).paginate(page, PER_PAGE, False).items
    pagination = Pagination(per_page=PER_PAGE, page=page, total=Note.query.filter(Note.customer_id.in_(ids)).count(), record_name='notes', css_framework='bootstrap4')

    form = CreateNoteForm(customer_id=form_customer_id)
    form.customer_id.choices = [("{}".format(c.id), c.instagram_login) for c in customers]

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

    return render_template(
        'notes.html',
        _menu='notes',
        form=form,
        notes=notes,
        customers=customers,
        project=project,
        pagination=pagination
    )