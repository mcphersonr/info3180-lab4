from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from werkzeug.utils import secure_filename



class UploadForm(FlaskForm):

	image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only')])
	details = StringField('Details', validators=[DataRequired()])