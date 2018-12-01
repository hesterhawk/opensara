from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import ValidationError, DataRequired, Length

from .url_validator import UrlValidator

class CreateNoteForm(FlaskForm):

    instagram_post_url = StringField('Instagram post url', validators=[Length(max=255)])    
    message = StringField('Message', widget=TextArea(), validators=[DataRequired(), Length(max=4000)])    
    state = IntegerField('State', validators=[DataRequired()])
    submit = SubmitField('Create new Note')

    def validate_instagram_post_url(self, instagram_post_url):        

        if '' == instagram_post_url.data: return True

        validator = UrlValidator(instagram_post_url.data)

        if validator.is_valid() is not True:
            raise ValidationError('Sorry my Friend, instagram login is in use')