from dataclasses import dataclass
from sqlalchemy import Column, BIGINT, Integer, String, SMALLINT, REAL, DATE, Boolean, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import login
from app import db


@dataclass()
class Volcano(db.Model):
    __tablename__ = 'Volcano'
    volcId = Column(BIGINT, primary_key=True)
    volcName = Column(String)
    volcNameLat = Column(String)
    volcShortName = Column(String)
    volcShortNameLat = Column(String)
    volcType = Column(SMALLINT)


@dataclass()
class VolcanoStation(db.Model):
    __tablename__ = "VolcanoStation"
    volcstId = Column(Integer, primary_key=True)
    volcstVolcanoId = Column(Integer, ForeignKey('Volcano.volcId'))
    volcstStationId = Column(Integer, ForeignKey('Station.stId'))
    volcstDistance = Column(REAL)
    volcstPreffered = Column(Boolean)


@dataclass()
class Station(db.Model):
    __tablename__ = 'Station'
    stId = Column(Integer, primary_key=True)
    stName = Column(String)
    stNameLat = Column(String)
    stRegionalCode = Column(String)
    stInternationalCode = Column(String)
    stInternationalCodeRegistered = Column(DATE)
    stComment = Column(String)
    stState = Column(Integer)


@dataclass()
class Network(db.Model):
    __tablename__ = "Network"
    netId = Column(Integer, primary_key=True)
    netName = Column(String)
    netRemId = Column(Integer)
    netNameLat = Column(String)
    netCode = Column(String)


@dataclass()
class Instrument(db.Model):
    __tablename__ = "Instrument"
    instId = Column(Integer, primary_key=True)
    instNetId = Column(Integer, ForeignKey('NetworkId'))
    instStId = Column(Integer, ForeignKey('Station.stId'))
    instLocation = Column(Integer)
    instName = Column(String)
    instOrgId = Column(Integer, ForeignKey(''))
    instOrder = Column(Integer)


@dataclass()
class HypoCenter(db.Model):
    __tablename__ = "HypoCenter"
    hypId = Column(Integer, primary_key=True)


@dataclass()
class EventType(db.Model):
    __tablename__ = 'EventType'
    typeId = Column(Integer, primary_key=True)
    type = Column(String)


@dataclass()
class NoteVideoObs(db.Model):
    __tablename__ = "NoteVideoObs"
    nvoId = Column(Integer, primary_key=True)
    nvoNote = Column(String)
    nvoRelevanceNote = Column(Boolean)
    nvoOperatorId = Column(Integer, ForeignKey('Operator.opId'))
    nvoDateSave = Column(DATE)

    @staticmethod
    def add(note, relevance, opId):
        nvo = NoteVideoObs(
            nvoNote=note,
            nvoRelevanceNote=relevance,
            nvoOperatorId=opId,
            nvoDateSave=datetime.now()
        )
        try:
            db.session.add(nvo)
            db.session.commit()
        except:
            print('error database')

    @staticmethod
    def get_id(note, relevance, opId):
        nvo = NoteVideoObs.query.filter_by(
            nvoNote=note,
            nvoRelevanceNote=relevance,
            nvoOperatorId=opId
        )

        return nvo.nvoId


@dataclass()
class Camera(db.Model):
    __tablename__ = "Camera"
    cmId = Column(Integer, primary_key=True)
    cmName = Column(String)


class Operator(db.Model, UserMixin):
    __tablename__ = 'Operator'
    opId = Column(Integer, primary_key=True)
    opSurname = Column(String)
    opPasswordHash = Column(String)

    def get_id(self):
        return self.opId

    def setPassword(self, password):
        self.opPasswordHash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.opPasswordHash, password)


@login.user_loader
def load_user(id):
    return Operator.query.get(int(id))

@dataclass()
class VolcanoOperator(db.Model):
    __tablename__ = "VolcanoOperator"
    volcopId = Column(Integer, primary_key=True)
    volcopVolcanoId = Column(Integer, ForeignKey('Volcano.volcId'))
    volcopOperatorId = Column(Integer, ForeignKey('Operator.opId'))


@dataclass()
class Observation(db.Model):
    __tablename__ = "Observation"
    obsId = Column(Integer, primary_key=True)
    obsDate = Column(DATE)
    obsVolcanoId = Column(Integer, ForeignKey('Volcano.volcId'))
    obsOperatorId = Column(Integer, ForeignKey('Operator.opId'))
    obsCreatedBy = Column(String)
    obsDateSave = Column(DATE)

    @staticmethod
    def is_check(opId, date, volcId):
        obs = Observation()

        if obs.query.filter_by(obsOperatorId=opId, obsDate=date, obsVolcanoId=volcId).first() is None:
            return False
        else:
            return True

    @staticmethod
    def add (opId, date, volcId, createdBy):
        dateServer = datetime.now()
        obs = Observation(obsDate=date,
                          obsVolcanoId=volcId,
                          obsOperatorId=opId,
                          obsCreatedBy=createdBy,
                          obsDateSave=dateServer)
        try:
            db.session.add(obs)
            db.session.commit()
            observation = obs  # для дальнейшего заполнения seisobs
        except:
            print('error database')

    @staticmethod
    def get_id(opId, date, volcId):
        observation = Observation.query.filter_by(obsOperatorId=opId, obsDate=date,
                                                  obsVolcanoId=volcId).first()
        return observation.obsId


@dataclass()
class VideoObservation(db.Model):
    __tablename__ = "VideoObservation"
    vobsId = Column(Integer, primary_key=True)
    vobsObservationId = Column(Integer, ForeignKey(''))
    vobsHeightDischarge = Column(SMALLINT)
    vobsNvoId = Column(Integer, ForeignKey('NoteVideoObs,nvoId'))
    vobsCmId = Column(Integer, ForeignKey('Camera.cmId'))
    vobsOperatorId = Column(Integer, ForeignKey('Operator.opId'))
    vobsDateSave = Column(DATE)


@dataclass()
class SatelliteObservation(db.Model):
    __tablename__ = "SatelliteObservation"
    satobsId = Column(Integer, primary_key=True)
    satobsObservationId = Column(Integer, ForeignKey('Observation.obsId'))
    satobsPixels = Column(SMALLINT)
    satobsTmax = Column(SMALLINT)
    satobsTfon = Column(SMALLINT)
    satobsOperatorId = Column(Integer, ForeignKey('Operator.opId'))


@dataclass()
class SeismicObservation(db.Model):
    __tablename__ = "SeismicObservation"
    seisobsId = Column(Integer, primary_key=True)
    seisobsObservationId = Column(Integer, ForeignKey('Observation.obsId'))
    seisobsStationId = Column(Integer, ForeignKey('Station.stId'))
    seisobsInstrumentId = Column(Integer, ForeignKey('Instrument.instId'))
    seisobsOperatorId = Column(Integer, ForeignKey('Operator.opId'))
    seisobsStartTime = Column(DATE)
    seisobsEndTime = Column(DATE)
    seisobsPeriodStartTime = Column(DATE)
    seisobsPeriodEndTime = Column(DATE)
    seisobsHypocenterId = Column(Integer, ForeignKey('HypoCenter.hypId'))
    seisobsEventCount = Column(SMALLINT)
    seisobsWeak = Column(Boolean)
    seisobsEventTypeId = Column(Integer, ForeignKey('EventType.typeId'))
    seisobsAvgAT = Column(REAL)
    seisobsMaxAT = Column(REAL)
    seisobsDuration = Column(SMALLINT)
    seisobsEnergyClass = Column(REAL)
    seisobsDateSave = Column(DATE)
