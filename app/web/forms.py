from flask_wtf import FlaskForm
from wtforms import TimeField, FileField, SelectField, BooleanField, DateTimeField, DateField, SubmitField, StringField, IntegerField, SubmitField, FloatField, DateField
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
    vobsFilePath = StringField('Путь к изображению')
    vobsHeightDischarge = FloatField('Высота пебловых выбросов')
    nvoNote = StringField('Примечание')
    sub_add = SubmitField('Добавить')

class SatelliteObservationForm(FlaskForm):
    volcanoId = SelectField('Вулкан')
    satobsPixels = IntegerField('Количество пикселей')
    satobsTmax = FloatField('Максимальная  температура фона(Tmax)')
    satobsTfon = FloatField('Средняя температура фона(Tfon)')
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
    seisobsDuration = FloatField('Продолжительность', validators=None)
    sub_add = SubmitField('Добавить')

class HazardCodeForm(FlaskForm):
    volcanoId = SelectField('Вулкан')
    codeObsId = StringField('Дата')
    codeType = SelectField('код опасности')



class PeriodForOutDataForm(FlaskForm):
    periodStart = StringField("С ")
    periodEnd = StringField("    По ")
    subOut = SubmitField('Вывести')
