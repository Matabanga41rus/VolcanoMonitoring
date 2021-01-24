from flask_wtf import FlaskForm
from wtforms import TimeField, SelectField, DateField, SubmitField, StringField, IntegerField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired

class ObservationForm(FlaskForm):
    obsDate = DateField('Дата', validators=[DataRequired()])
    obsVolcanoId = SelectField('Вулкан', validators=[DataRequired()])
    obsCode = StringField('Код опасности', validators=[DataRequired()])

class SeismicObservationForm(FlaskForm):
    seisobsStationId = SelectField('Станция', validators=[DataRequired()])
    seisobsStartTime = TimeField('От', validators=[DataRequired()])
    seisobsEndTime = TimeField('До', validators=[DataRequired()])
    seisobsHypocenter = StringField('Эпицентр', validators=[DataRequired()])
    seisobsWeakEventCount = StringField('Кол-во слабых событий', validators=[DataRequired()])
    seisobsStrongEventCount = StringField('Кол-во сильныхсобытий', validators=[DataRequired()])
    seisobsTypeEventId = SelectField('Тип события')
    seisobsAvgAT = FloatField('Среднее А/Т', validators=[DataRequired()])
    seisobsMaxAT =FloatField('Максимальное А/Т', validators=[DataRequired()])
    seisobsDuration = FloatField('Продолжительность', validators=[DataRequired()])
    sub_add = SubmitField('Добавить')

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
    sub_add = SubmitField('Добавь')