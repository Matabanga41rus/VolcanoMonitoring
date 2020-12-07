from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired

class VolcanoForm(FlaskForm):
    namev = StringField('Название', validators=[DataRequired()])
    latitude = FloatField('Широта', validators=[DataRequired()])
    longitude = FloatField('Долгота', validators=[DataRequired()])
    height = IntegerField('Высота (в метрах)', validators=[DataRequired()])
    sub_add = SubmitField('Добавить')

class StateVolcanoForm(FlaskForm):
    namev = StringField('Название', validators=[DataRequired()])
    date_state = StringField('Дата', validators=[DataRequired()])
    thermal_anomaly = IntegerField('Термальная аномалия', validators=[DataRequired()])
    number_events = IntegerField('Количество событий', validators=[DataRequired()])
    max_pgd_height = IntegerField('Макс. высота ПГД ', validators=[DataRequired()])
    observ_ash_emissions = StringField('Наблюдаемые пепловые выбросы', validators=[DataRequired()])
    hazard_code = StringField('Код опасности', validators=[DataRequired()])
    sub_add = SubmitField('Добавить')