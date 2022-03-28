from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = IntegerField('ID Тим Лидера', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField('Время на выполнение работы', validators=[DataRequired()])
    collaborators = StringField("ID участников", validators=[DataRequired()])
    start_date = DateField("Начало работы")
    end_date = DateField("Конеч работы")
    is_finished = BooleanField("Завершена работа?")

    submit = SubmitField('Зарегестрироваться')
