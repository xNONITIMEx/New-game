from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class AnswerForm(FlaskForm):
    motivation = TextAreaField('Опишите, пожалуйста проблему:', validators=[DataRequired()])
    submit = SubmitField('Войти')
