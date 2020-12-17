from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, SMALLINT, REAL, DATE, Boolean, ForeignKey
from app import db

@dataclass()
class Volcano(db.Model):
    volcID: Column(Integer, primary_key=True)
    volcRuName: Column(String)
    volcEnName: Column(String)
    volcHeight: Column(SMALLINT)
    volcLongitude: Column(REAL)
    volcLatitude: Column(REAL)


@dataclass()
class VolcanoStation(db.Model):
    volcstVolcanoId: Column(Integer)
    volcstStationId: Column(Integer)
    volcstDistance: Column(REAL)
    volcstPreffered: Column(Boolean)


@dataclass()
class Station(db.Model):
    stId: Column(Integer)


@dataclass()
class Instrument(db.Model):
    instId: Column(Integer)


@dataclass()
class HypoCenter(db.Model):
    hypId: Column(Integer)


@dataclass()
class SeismicEventType(db.Model):
    typeId: Column(Integer)
    type: Column(String)


@dataclass()
class NoteVideoObs(db.Model):
    nvoId: Column(Integer)
    nvoNote: Column(String)
    nvoRelevanceNote: Column(Boolean)


@dataclass()
class Camera(db.Model):
    cmId: Column(Integer)
    cmName: Column(String)


@dataclass()
class Operator(db.Model):
    opId: Column(Integer)


@dataclass()
class Observation(db.Model):
    obsId: Column(Integer)
    obsDate: Column(DATE)
    obsVolcanoID: Column(Integer, ForeignKey('Volcano.volcId'))
    obsOperatorID: Operator
    obsCode: Column(String)


@dataclass()
class VideoObservation(db.Model):
    vobsId: Column(Integer)
    vobsObservationId: Observation
    vobsHeightDischarge: Column(SMALLINT)
    vobsNvoId: NoteVideoObs
    vobsCmId:Camera


@dataclass()
class SatelliteObservation(db.Model):
    satobsId: Column(Integer)
    satobsObservationId: Observation
    satobsPixels: Column(SMALLINT)
    satobsTmax: Column(SMALLINT)
    satobsTfon: Column(SMALLINT)


@dataclass()
class SeismicObservation(db.Model):
    seisobsId: Column(Integer)
    seisobsObservationId: Observation
    seisobsStationId: Station
    seisobsInstrumentId: Instrument
    seisobsTimeStamp: Column(SMALLINT)
    seisobsHypocenter: HypoCenter
    seisobsWeakEventCount: Column(SMALLINT)
    seisobsStrongEventCount: Column(SMALLINT)
    seisobsTypeEventId: SeismicEventType
    seisobsAvgAT: Column(REAL)
    seisobsMaxAT: Column(REAL)
    seisobsSumAT: Column(REAL)
    seisobsDuration: Column(SMALLINT)




