from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField


class LoginForm(FlaskForm):
    f_name = StringField('Имя', validators=[DataRequired()])
    s_name = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    gender = SelectField(
        label='Пол',
        coerce=str,
        choices=['Мужской', 'Женский'],
        validators=[DataRequired()]
    )
    profesional = SelectField(
        label='Профессия',
        coerce=str,
        choices=["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
                 "климатолог", "специалист по радиационной защите", "астрогеолог", "инженер жизнеобеспечения"],
        validators=[DataRequired()]
    )
    motiv = TextAreaField('Мотивация')
    photo = FileField('Фото')
    save = BooleanField('Готовы ли вы остаться на марсе?')
    submit = SubmitField('Зарегестрироваться')
