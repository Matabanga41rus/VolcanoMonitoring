from flask_wtf import FlaskForm
from wtforms import TimeField, SelectField, BooleanField, DateTimeField, DateField, SubmitField, StringField, IntegerField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    opSurname = StringField('Фамилия')
    opPassword = StringField('Пароль')
    login = SubmitField('Войти')

class SeismicObservationForm(FlaskForm):
    volcanoId = SelectField('Вулкан')
    seisobsStationId = SelectField('Станция')
    seisobsEventTypeId = SelectField('Тип события')
    seisobsStartTime = StringField('От', validators=[DataRequired()])
    seisobsEndTime = StringField('До', validators=[DataRequired()])
    seisobsPeriodStartTime = StringField('Период от', validators=[DataRequired()])
    seisobsPeriodEndTime = StringField('Период до', validators=[DataRequired()])
    seisobsEventCount = StringField('Кол-во событий', validators=[DataRequired()])
    seisobsWeak = BooleanField('Слабое(ые) событие(я)?')
    seisobsAvgAT = FloatField('Среднее А/Т', validators=[DataRequired()])
    seisobsMaxAT =FloatField('Максимальное А/Т', validators=[DataRequired()])
    seisobsEnergyClass = FloatField('Энергетический класс', validators=[DataRequired()])
    seisobsDuration = FloatField('Продолжительность')
    sub_add = SubmitField('Добавить')


