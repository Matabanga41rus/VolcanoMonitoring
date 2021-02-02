# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash
from datetime import datetime
from app import app, db
from app.web.forms import SeismicObservationForm, LoginForm
from flask_login import current_user, login_user, logout_user
from app.web.models import SeismicObservation, EventType, Station, Observation, Operator, Volcano


@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        return render_template('index.html')

    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
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

@app.route('/add', methods=['GET','POST'])
def add():
    todayDate = datetime.now()
    opId = current_user.opId

    volcanoAll = Volcano.query.all()

    volcanoList = [(volc.volcId, volc.volcName) for volc in volcanoAll]
    stationList = [(st.stId, st.stName) for st in Station.query.all()]
    eventTypeList = [(tp.typeId, tp.type) for tp in EventType.query.all()]

    seisFormAdd = SeismicObservationForm()
    seisFormAdd.volcanoId.choices = volcanoList
    seisFormAdd.seisobsStationId.choices = stationList
    seisFormAdd.seisobsEventTypeId.choices = eventTypeList

    if seisFormAdd.validate_on_submit():
        observation = Observation.query.filter_by(obsOperatorId=opId, obsDate=todayDate.date(), obsVolcanoId=seisFormAdd.volcanoId.data).first()

        if observation is None:
            obs = Observation(obsDate=todayDate.date(),
                              obsVolcanoId=seisFormAdd.volcanoId.data,
                              obsOperatorId=opId)
            try:
                db.session.add(obs)
                db.session.commit()
                observation = obs
            except:
                print('error database')

        seisObs = SeismicObservation(
            seisobsObservationId=observation.obsId,
            seisobsStationId=seisFormAdd.seisobsStationId.data,
            seisobsInstrumentId=None,
            seisobsOperatorId=opId,
            seisobsStartTime=todayDate,
            seisobsEndTime=todayDate,
            seisobsPeriodStartTime=todayDate,
            seisobsPeriodEndTime=todayDate,
            seisobsHypocenterId=None,
            seisobsEventCount=seisFormAdd.seisobsEventCount.data,
            seisobsWeak=seisFormAdd.seisobsWeak.data,
            seisobsEventTypeId=seisFormAdd.seisobsEventTypeId.data,
            seisobsAvgAT=seisFormAdd.seisobsAvgAT.data,
            seisobsMaxAT=seisFormAdd.seisobsMaxAT.data,
            seisobsEnergyClass=seisFormAdd.seisobsEnergyClass.data,
            seisobsDuration=seisFormAdd.seisobsDuration.data,
            seisobsDateSave=todayDate

        )
        try:
            db.session.add(seisObs)
            db.session.commit()
        except:
            print('error database')


    return render_template('add.html', form=seisFormAdd, date=todayDate.date())
