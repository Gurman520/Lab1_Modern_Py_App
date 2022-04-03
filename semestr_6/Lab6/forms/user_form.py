from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    email = StringField('Login/Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    s_name = StringField('Фамилия', validators=[DataRequired()])
    f_name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired()])
    position = StringField("Должность", validators=[DataRequired()])
    speciality = StringField("Профессия", validators=[DataRequired()])
    addres = StringField("Адрес", validators=[DataRequired()])

    submit = SubmitField('Зарегестрироваться')
