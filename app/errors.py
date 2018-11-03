from flask import render_template
from app import app, db

from app.config.app import Config

@app.errorhandler(404)
def not_found_error(error):
    return render_template('dashboard/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('dashboard/500.html'), 500