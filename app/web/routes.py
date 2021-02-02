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

@app.route('/add')
def index():
    obsFormAdd = ObservationForm()


    seisFormAdd = SeismicObservationForm()
    if(seisFormAdd.validate_on_submit()):
        seism = SeismicObservationForm(
        )


    return render_template('add.html')
