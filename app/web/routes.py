# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash
from datetime import datetime
from app import app, db
from app.web.forms import SeismicObservationForm, LoginForm, ObservationForm, VideoObservationForm, SatelliteObservationForm
from flask_login import current_user, login_user, logout_user
from app.web.models import SatelliteObservation, VideoObservation, NoteVideoObs,SeismicObservation, EventType, Station, Observation, Operator, Volcano, VolcanoOperator


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        operator = Operator.query.filter_by(opSurname=loginForm.opSurname.data).first()
        if operator is None or not operator.checkPassword(loginForm.opPassword.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(operator)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', loginForm=loginForm)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/observation', methods=['GET', 'POST'])
def addobservation():
    todayDate = datetime.now()
    operatorList = Operator.get_list_tuples_all_id_and_surname()
    volcanoList = Volcano.get_list_tuples_all_id_and_name()

    obsAddForm = ObservationForm()
    obsAddForm.obsOperatorId.choices = operatorList
    obsAddForm.obsVolcanoId.choices = volcanoList

    if obsAddForm.validate_on_submit():
        if not Observation.is_check(opId=obsAddForm.obsOperatorId.data, date=todayDate.date, volcId=obsAddForm.obsVolcanoId.data):
            Observation.add(opId=obsAddForm.obsOperatorId.data,
                            date=todayDate.date(),
                            volcId=obsAddForm.obsVolcanoId.data,
                            createdBy=current_user.opSurname)

    return render_template('addobservation.html', form=obsAddForm, date=todayDate.date())

@app.route('/observation/video', methods=['GET', 'POST'])
def addvideoobs():
    todayDate = datetime.now()
    opId = current_user.opId

    listIdVolcano = VolcanoOperator.get_list_id_volcano(opId)
    volcanoList = Volcano.get_list_tuples_id_and_name(listIdVolcano)

    vobsAddForm = VideoObservationForm()
    vobsAddForm.volcanoId.choices = volcanoList

    if vobsAddForm.validate_on_submit():
        if not Observation.is_check(opId=opId, date=todayDate.date(), volcId=vobsAddForm.volcanoId.data):
            Observation.add(opId=opId,
                            date=todayDate.date(),
                            volcId=vobsAddForm.obsVolcanoId.data,
                            createdBy=current_user.opSurname)

    return render_template('addvideoobs.html', form=vobsAddForm, date=todayDate.date())

@app.route('/observation/satellite', methods=['GET', 'POST'])
def addsatelliteobs():
    todayDate = datetime.now()
    opId = current_user.opId
    satobsAddForm = SatelliteObservationForm()

    listIdVolcano = VolcanoOperator.get_list_id_volcano(opId)
    volcanoList = Volcano.get_list_tuples_id_and_name(listIdVolcano)

    satobsAddForm.volcanoId.choices = volcanoList

    if satobsAddForm.validate_on_submit():
        volcId = satobsAddForm.volcanoId.data
        if not Observation.is_check(opId=opId, date=todayDate.date(), volcId=volcId):
            Observation.add(opId=opId, date=todayDate.date(), volcId=volcId, createdBy='automatic')

        obsId = Observation.get_id(opId=opId,date=todayDate.date(),volcId=volcId)
        SatelliteObservation.add(obsId=obsId,
                                 opId=opId,
                                 pixels=satobsAddForm.satobsPixels.data,
                                 Tmax=satobsAddForm.satobsTfon.data,
                                 Tfon=satobsAddForm.satobsTfon.data)

    return render_template('addsatelliteobs.html', form=satobsAddForm, date=todayDate.date())



@app.route('/observation/seismic', methods=['GET', 'POST'])
def addseismicobs():
    dateTimeServer = datetime.now()
    opId = current_user.opId

    listIdVolcano = VolcanoOperator.get_list_id_volcano(opId)

    volcanoList = Volcano.get_list_tuples_id_and_name(listIdVolcano)
    stationList = Station.get_list_tuples_all_id_and_name()
    eventTypeList = EventType.get_list_tuples_all_id_and_name()

    seisAddForm = SeismicObservationForm()
    seisAddForm.volcanoId.choices = volcanoList
    seisAddForm.seisobsStationId.choices = stationList
    seisAddForm.seisobsEventTypeId.choices = eventTypeList

    if seisAddForm.validate_on_submit():
        volcId = seisAddForm.volcanoId.data
        if not Observation.is_check(opId=opId, date=dateTimeServer.date(), volcId=volcId):
            Observation.add(opId=opId, date=dateTimeServer.date(), volcId=volcId, createdBy='automatic')

        obsId = Observation.get_id(opId=opId,date=dateTimeServer.date(), volcId=volcId)

        SeismicObservation.add(obsId=obsId,
                               stId=seisAddForm.seisobsStationId.data,
                               instId=None,
                               opId=opId,
                               startTime= dateTimeServer,
                               endTime=dateTimeServer,
                               periodStartTime=dateTimeServer,
                               periodEndTime=dateTimeServer,
                               hypId=None,
                               eventCount=seisAddForm.seisobsEventCount.data,
                               weak=seisAddForm.seisobsWeak.data,
                               eventTypeId=seisAddForm.seisobsEventTypeId.data,
                               avgAT=seisAddForm.seisobsAvgAT.data,
                               maxAT=seisAddForm.seisobsMaxAT.data,
                               energyClass=seisAddForm.seisobsEnergyClass.data,
                               duration=seisAddForm.seisobsDuration.data,
                               datesave=dateTimeServer)

    return render_template('addseismicobs.html', form=seisAddForm, date=dateTimeServer.date())
