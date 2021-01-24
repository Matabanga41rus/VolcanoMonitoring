# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from app.web.forms import SeismicObservationForm, ObservationForm
from app.web.models import SeismicObservation, Observation



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add')
def index():
    obsFormAdd = ObservationForm()


    seisFormAdd = SeismicObservationForm()
    if(seisFormAdd.validate_on_submit()):
        seism = SeismicObservationForm(
        )


    return render_template('add.html')
