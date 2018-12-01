from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime

from .forms.create import CreateNoteForm

note = Blueprint('note', __name__, template_folder="views")

from app import db
from app.models.note import Note
from app.models.customer import Customer

PER_PAGE = 10

@note.route('/notes/all/<customer_id>', methods=['GET', 'POST'])
def all(customer_id: int):
    customer = Customer.query.get(customer_id)
    
    page = request.args.get(get_page_parameter(), type=int, default=1)
    notes = Note.query.filter_by(customer_id=customer.id).order_by(Note.state).paginate(page, PER_PAGE, False).items
    pagination = Pagination(per_page=PER_PAGE, page=page, total=Note.query.count(), record_name='notes', css_framework='bootstrap4')

    form = CreateNoteForm()

    if form.validate_on_submit():
        note = Note(
            customer_id=customer.id, 
            state=form.state.data, 
            message=form.message.data, 
            created_date=datetime.now()
        )

        db.session.add(note)
        db.session.commit()

        flash("Note created successfully!")
        return redirect(url_for('note.all', customer_id=customer.id))

    return render_template(
        'notes.html',
        form=form,
        notes=notes,
        customer=customer,
        pagination=pagination
    )