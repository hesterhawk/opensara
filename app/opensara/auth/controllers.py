from flask import Blueprint, current_app, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from .forms.login import LoginForm

auth = Blueprint('auth', __name__, template_folder="views")

from app import db
from app.models.user import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('project.all'))

    form = LoginForm()    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Wrong login or password")
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me)
        return redirect(url_for('project.all'))

    return render_template('login.html', form=form)


@auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))