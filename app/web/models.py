from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, SMALLINT, REAL, DATE, Boolean, ForeignKey
from app import db

@dataclass()
class Volcano(db.Model):
    volcId: Column(Integer, primary_key=True)
    volcName: Column(String)
    volcNameLat: Column(String)
    volcShortName: Column(String)
    volcShortNameLat: Column(String)
    volcType: Column(SMALLINT)


@dataclass()
class VolcanoStation(db.Model):
    volcstId: Column(Integer, primary_key=True)
    volcstVolcanoId: Column(Integer, ForeignKey('Volcano.volcId'))
    volcstStationId: Column(Integer, ForeignKey('Station.stId'))
    volcstDistance: Column(REAL)
    volcstPreffered: Column(Boolean)


@dataclass()
class Station(db.Model):
    stId: Column(Integer, primary_key=True)
    stName: Column(String)
    stNameLat: Column(String)
    stRegionalCode: Column(String)
    stInternationalCode: Column(String)
    stInternationalCodeRegistered: Column(DATE)
    stComment: Column(String)
    stState: Column(Integer)


@dataclass()
class Network(db.Model):
    netId: Column(Integer, primary_key=True)
    netName: Column(String)
    netRemId: Column(Integer)
    netNameLat: Column(String)
    netCode: Column(String)

@dataclass()
class Instrument(db.Model):
    instId: Column(Integer, primary_key=True)
    instNetId: Column(Integer, ForeignKey('NetworkId'))
    instStId: Column(Integer, ForeignKey('Station.stId'))
    instLocation: Column(Integer)
    instName: Column(String)
    instOrgId: Column(Integer, ForeignKey(''))
    instOrder: Column(Integer)


@dataclass()
class HypoCenter(db.Model, primary_key=True):
    hypId: Column(Integer)


@dataclass()
class SeismicEventType(db.Model):
    typeId: Column(Integer, primary_key=True)
    type: Column(String)


@dataclass()
class NoteVideoObs(db.Model):
    nvoId: Column(Integer, primary_key=True)
    nvoNote: Column(String)
    nvoRelevanceNote: Column(Boolean)


@dataclass()
class Camera(db.Model):
    cmId: Column(Integer, primary_key=True)
    cmName: Column(String)


@dataclass()
class Operator(db.Model):
    opId: Column(Integer, primary_key=True)


@dataclass()
class Observation(db.Model):
    obsId: Column(Integer, primary_key=True)
    obsDate: Column(DATE)
    obsVolcanoId: Column(Integer, ForeignKey('Volcano.volcId'))
    obsOperatorId: Column(Integer, ForeignKey('OperatorId'))
    obsCode: Column(String)


@dataclass()
class VideoObservation(db.Model, primary_key=True):
    vobsId: Column(Integer)
    vobsObservationId: Column(Integer, ForeignKey(''))
    vobsHeightDischarge: Column(SMALLINT)
    vobsNvoId: Column(Integer, ForeignKey('NoteVideoObs,nvoId'))
    vobsCmId: Column(Integer, ForeignKey('Camera.cmId'))


@dataclass()
class SatelliteObservation(db.Model):
    satobsId: Column(Integer, primary_key=True)
    satobsObservationId: Column(Integer, ForeignKey('Observation.obsId'))
    satobsPixels: Column(SMALLINT)
    satobsTmax: Column(SMALLINT)
    satobsTfon: Column(SMALLINT)


@dataclass()
class SeismicObservation(db.Model):
    seisobsId: Column(Integer, primary_key=True)
    seisobsObservationId: Column(Integer, ForeignKey('Observation.obsId'))
    seisobsStationId: Column(Integer, ForeignKey('Station.stId'))
    seisobsInstrumentId: Column(Integer, ForeignKey('Instrument.instId'))
    seisobsStartTime: Column(DATE)
    seisobsEndTime: Column(DATE)
    seisobsHypocenter: Column(Integer, ForeignKey('HypoCenter'))
    seisobsWeakEventCount: Column(SMALLINT)
    seisobsStrongEventCount: Column(SMALLINT)
    seisobsTypeEventId: Column(Integer, ForeignKey('TypeEvent'))
    seisobsAvgAT: Column(REAL)
    seisobsMaxAT: Column(REAL)
    seisobsDuration: Column(SMALLINT)




