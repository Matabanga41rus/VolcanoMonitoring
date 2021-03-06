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

    @staticmethod
    def get_list_tuples_all_id_and_name():
        list = []
        for vl in Volcano.query.all():
            list.append((vl.volcId, vl.volcName))
        return list

    @staticmethod
    def get_list_tuples_id_and_name(listId):
        list = []
        for id in listId:
            vl = Volcano.query.get(id)
            list.append((vl.volcId, vl.volcName))
        return list


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

    @staticmethod
    def get_list_tuples_all_id_and_name():
        list = []
        for st in Station.query.all():
            list.append((st.stId, st.stName))
        return list


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

    @staticmethod
    def get_list_tuples_all_id_and_name():
        list = []
        for tp in EventType.query.all():
            list.append((tp.typeId, tp.type))
        return list


@dataclass()
class NoteVideoObs(db.Model):
    __tablename__ = "NoteVideoObs"
    nvoId = Column(Integer, primary_key=True)
    nvoVideoObsId = Column(Integer, ForeignKey('VideoObservation.vobsId'))
    nvoNote = Column(String)
    nvoRelevanceNote = Column(Boolean)
    nvoOperatorId = Column(Integer, ForeignKey('Operator.opId'))
    nvoDateSave = Column(DATE)

    @staticmethod
    def add(vobsId, note, relevance, opId):
        nvo = NoteVideoObs(
            nvoVideoObsId=vobsId,
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
    def get_id(vobsId, note, relevance, opId):
        nvo = NoteVideoObs.query.filter_by(nvoVideoObsId=vobsId,
                                           nvoNote=note,
                                           nvoRelevanceNote=relevance,
                                           nvoOperatorId=opId)

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

    @staticmethod
    def get_list_tuples_all_id_and_surname():
        list = []
        for op in Operator.query.all():
            list.append((op.opId, op.opSurname))
        return list

    def get_id(self):
        return self.opId

    def set_password(self, password):
        self.opPasswordHash = generate_password_hash(password)

    def check_password(self, password):
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

    @staticmethod
    def get_list_id_volcano(opId):
        volcop = VolcanoOperator.query.filter_by(volcopOperatorId=opId)
        listId = []
        for vp in volcop:
            listId.append(vp.volcopVolcanoId)
        return listId


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
        return Observation.query.filter_by(obsOperatorId=opId, obsDate=date, obsVolcanoId=volcId).first() is not None

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
    vobsObservationId = Column(Integer, ForeignKey('Observation.obsId'))
    vobsHeightDischarge = Column(SMALLINT)
    vobsFilePath = Column(String)
    vobsCmId = Column(Integer, ForeignKey('Camera.cmId'))
    vobsOperatorId = Column(Integer, ForeignKey('Operator.opId'))
    vobsDateSave = Column(DATE)

    @staticmethod
    def add(obsId, heightDischarge, filePath, cmId, opId):
        vobs = VideoObservation(
            vobsObservationId=obsId,
            vobsHeightDischarge=heightDischarge,
            vobsFilePath=filePath,
            vobsCmId=cmId,
            vobsOperatorId=opId,
            vobsDateSave= datetime.now()
        )

        try:
            db.session.add(vobs)
            db.session.commit()
        except:
            print('error database')

    @staticmethod
    def get_id(obsId, heightDischarge, filePath, cmId, opId):
        vobs = VideoObservation.query.filter_by(vobsObservationId=obsId,
                                             vobsHeightDischarge=heightDischarge,
                                             vobsFilePath=filePath,
                                             vobsCmId=cmId,
                                             vobsOperatorId=opId).first()

        return vobs.vobsId

    @staticmethod
    def getListLastVobs(count):
        listVobs = db.session.query(Observation, Operator, Volcano,VideoObservation, NoteVideoObs). \
            filter(VideoObservation.vobsObservationId == Observation.obsId). \
            filter(NoteVideoObs.nvoVideoObsId == VideoObservation.vobsId). \
            filter(Observation.obsVolcanoId == Volcano.volcId). \
            filter(Observation.obsOperatorId == Operator.opId).\
            order_by(db.desc(VideoObservation.vobsId)).limit(count)
        return listVobs

    @staticmethod
    def getListVobsForPeriod(periodStart, periodEnd):
        listVobs = db.session.query(Observation, Volcano, VideoObservation, NoteVideoObs). \
            filter(VideoObservation.vobsObservationId == Observation.obsId). \
            filter(NoteVideoObs.nvoVideoObsId == VideoObservation.vobsId). \
            filter(Observation.obsVolcanoId == Volcano.volcId). \
            filter(Observation.obsOperatorId == Operator.opId). \
            filter(Observation.obsDate >= periodStart). \
            filter(Observation.obsDate <= periodEnd).all()

        return listVobs


@dataclass()
class SatelliteObservation(db.Model):
    __tablename__ = "SatelliteObservation"
    satobsId = Column(Integer, primary_key=True)
    satobsOperatorId = Column(Integer, ForeignKey('Operator.opId'))
    satobsObservationId = Column(Integer, ForeignKey('Observation.obsId'))
    satobsPixels = Column(SMALLINT)
    satobsTmax = Column(SMALLINT)
    satobsTfon = Column(SMALLINT)
    satobsDateSave = Column(DATE)

    @staticmethod
    def add(obsId, opId, pixels, Tmax, Tfon):
        dateServer = datetime.now()
        satobs = SatelliteObservation(
            satobsObservationId=obsId,
            satobsOperatorId=opId,
            satobsPixels=pixels,
            satobsTmax=Tmax,
            satobsTfon=Tfon,
            satobsDateSave=dateServer
        )

        try:
            db.session.add(satobs)
            db.session.commit()
        except:
            print('error database')

    @staticmethod
    def getListLastSatobs(count):
        listSatobs = db.session.query(Observation, Volcano, Operator, SatelliteObservation). \
            filter(SatelliteObservation.satobsObservationId == Observation.obsId). \
            filter(Observation.obsVolcanoId == Volcano.volcId). \
            filter(Observation.obsOperatorId == Operator.opId).order_by(db.desc(SatelliteObservation.satobsId)).limit(
            count)

        return listSatobs

    @staticmethod
    def getListSatobsForPeriod(periodStart, periodEnd):
        listSatobs = db.session.query(Observation, Volcano, Operator, SatelliteObservation). \
            filter(SatelliteObservation.satobsObservationId == Observation.obsId). \
            filter(Observation.obsVolcanoId == Volcano.volcId). \
            filter(Observation.obsOperatorId == Operator.opId). \
            filter(Observation.obsDate >= periodStart). \
            filter(Observation.obsDate <= periodEnd).all()

        return listSatobs


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

    @staticmethod
    def add(obsId, stId, instId, opId, startTime, endTime, periodStartTime, periodEndTime,
            hypId, eventCount, weak, eventTypeId,  avgAT, maxAT, duration, energyClass, datesave):
        seisObs = SeismicObservation(
            seisobsObservationId=obsId,
            seisobsStationId=stId,
            seisobsInstrumentId=instId,
            seisobsOperatorId=opId,
            seisobsStartTime=startTime,
            seisobsEndTime=endTime,
            seisobsPeriodStartTime=periodStartTime,
            seisobsPeriodEndTime=periodEndTime,
            seisobsHypocenterId=hypId,
            seisobsEventCount=eventCount,
            seisobsWeak=weak,
            seisobsEventTypeId=eventTypeId,
            seisobsAvgAT=avgAT,
            seisobsMaxAT=maxAT,
            seisobsEnergyClass=energyClass,
            seisobsDuration=duration,
            seisobsDateSave=datesave
        )
        try:
            db.session.add(seisObs)
            db.session.commit()
        except:
            print('error database')

    @staticmethod
    def get_list_last_sesmicobs(count):
        listSeisobs = db.session.query(Observation, Station, Volcano, Operator, SeismicObservation, EventType). \
            filter(SeismicObservation.seisobsObservationId == Observation.obsId). \
            filter(SeismicObservation.seisobsEventTypeId == EventType.typeId). \
            filter(SeismicObservation.seisobsStationId == Station.stId). \
            filter(Observation.obsVolcanoId == Volcano.volcId). \
            filter(Observation.obsOperatorId == Operator.opId).\
            order_by(db.desc(SeismicObservation.seisobsId)).limit(count)

        return listSeisobs

    @staticmethod
    def get_list_satobs_for_period(periodStart, periodEnd):
        listSeisobs = db.session.query(Observation, Station, Volcano, Operator, SeismicObservation, EventType). \
            filter(SeismicObservation.seisobsObservationId == Observation.obsId). \
            filter(SeismicObservation.seisobsEventTypeId == EventType.typeId). \
            filter(SeismicObservation.seisobsStationId == Station.stId). \
            filter(Observation.obsVolcanoId == Volcano.volcId). \
            filter(Observation.obsOperatorId == Operator.opId). \
            filter(Observation.obsDate >= periodStart). \
            filter(Observation.obsDate <= periodEnd).all()

        return listSeisobs

@dataclass()
class HazardCode(db.Model):
    __tablename__ = "HazardCode"
    codId = Column(Integer, primary_key=True)
    codType = Column(String)
    codObsId = Column(Integer, ForeignKey('Observation.obsId'))
    codOperatorId = Column(Integer, ForeignKey('Operator.opId'))
    codDataSave = Column(DATE)

    @staticmethod
    def add():


    @staticmethod
    def get_list_last_code(count):
        listCode =db.session.query(HazardCode, Observation, Volcano, Operator). \
            filter(HazardCode.codObsId == Observation.obsId). \
            filter(Observation.obsVolcanoId == Volcano.volcId). \
            filter(Observation.obsOperatorId == Operator.opId).order_by(db.desc(SatelliteObservation.satobsId)).limit(
            count)

        return listCode

    @staticmethod
    def get_list_code_for_period(periodStart, periodEnd):
        listCode = db.session.query(Observation, Volcano, Operator, HazardCode). \
            filter(HazardCode.codObsId == Observation.obsId). \
            filter(Observation.obsVolcanoId == Volcano.volcId). \
            filter(Observation.obsOperatorId == Operator.opId). \
            filter(Observation.obsDate >= periodStart). \
            filter(Observation.obsDate <= periodEnd).all()

        return listCode
