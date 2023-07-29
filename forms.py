from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, DateField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from flask_wtf.file import FileAllowed, FileRequired

class logFile(FlaskForm):
    transaction_data = FileField('Transaction Data', validators=[ DataRequired(message="passport photo"), FileAllowed([ 'csv'], 'Supports only CSV files!')])
    submit  = SubmitField(label="Load Data")