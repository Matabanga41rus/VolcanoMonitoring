from dataclasses import dataclass


@dataclass()
class Volcano:
    volcID: int
    volcRuName: str
    volcEnName: str
    volcHeight: int
    volcLongitude: float
    volcLatitude: float


@dataclass()
class VolcanoStation:
    volcstVolcanoId: int
    volcstStationId: int
    volcstDistance: float
    volcstPreffered: bool


@dataclass()
class Station:
    stId: int


@dataclass()
class Instrument:
    instId: int


@dataclass()
class HypoCenter:
    hypId: int


@dataclass()
class SeismicEventType:
    typeId: int
    type: str


@dataclass()
class NoteVideoObs:
    nvoId: int
    nvoNote: str
    nvoRelevanceNote: bool


@dataclass()
class Camera:
    cmId: int
    cmName: str


@dataclass()
class Operator:
    opId: int


@dataclass()
class Observation:
    obsId: int
    obsDate: int
    obsVolcanoID: Volcano
    obsOperatorID: Operator
    obsCode: str


@dataclass()
class VideoObservation:
    vobsId: int
    vobsObservationId: Observation
    vobsHeightDischarge: int
    vobsNvoId: NoteVideoObs
    vobsCmId:Camera


@dataclass()
class SatelliteObservation:
    satobsId: int
    satobsObservationId: Observation
    satobsPixels: int
    satobsTmax: int
    satobsTfon: int


@dataclass()
class SeismicObservation:
    seisobsId: int
    seisobsObservationId: Observation
    seisobsStationId: Station
    seisobsInstrumentId: Instrument
    seisobsTimeStamp: int
    seisobsHypocenter: HypoCenter
    seisobsWeakEventCount: int
    seisobsStrongEventCount: int
    seisobsTypeEventId: SeismicEventType
    seisobsAvgAT: float
    seisobsMaxAT: float
    seisobsSumAT: float
    seisobsDuration: int




