from flask_wtf import FlaskForm
from wtforms import TimeField, SelectField, BooleanField, DateTimeField, DateField, SubmitField, StringField, IntegerField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    opSurname = StringField('Фамилия')
    opPassword = StringField('Пароль')
    login = SubmitField('Войти')

class ObservationForm(FlaskForm):
    obsDate = StringField('Дата', validators=[DataRequired()])
    obsVolcanoId = SelectField('Вулкан')
    obsOperatorId = SelectField('Оператор')
    sub_add = SubmitField('Добавить')

class VideoObservationForm(FlaskForm):
    volcanoId = SelectField('Вулкан')
    vobsHeightDischarge = FloatField('Высота пебловых выбросов')
    nvoNote = StringField('Примечание')
    sub_add = SubmitField('Добавить')



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


