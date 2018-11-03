from flask import Blueprint, current_app, render_template, redirect, url_for
from flask_login import current_user

main = Blueprint('main', __name__, template_folder="views")

@main.route('/', methods=['GET'])
def index():
    return render_template('main.html')

@main.route('/dashboard', methods=['GET'])
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('dashboard.html')    