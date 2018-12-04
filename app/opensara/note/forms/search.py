from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import ValidationError, DataRequired, Length

from app.config.dashboard import Notes

from .url_validator import UrlValidator

class SearchNotesForm(FlaskForm):
    
    c = SelectField('State')
    s = SelectField('State', choices = Notes.state)