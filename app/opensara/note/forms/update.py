from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length

from app.config.dashboard import Notes

from .url_validator import UrlValidator

from app.models.note import Note

class UpdateNoteForm(FlaskForm):

    state = SelectField('State',
        default=0,
        choices = Notes.state,
        validators=[DataRequired()]
    )
    instagram_post_url = StringField('Instagram post url', validators=[Length(max=255)])        
    message = TextAreaField('message', validators=[Length(max=8000)])
    submit = SubmitField('Create new Note')

    def validate_instagram_post_url(self, instagram_post_url):        

        if '' == instagram_post_url.data: return True

        validator = UrlValidator(instagram_post_url.data)

        if validator.is_valid() is not True:
            raise ValidationError('Sorry my Friend, instagram login is in use')