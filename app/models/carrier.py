from app import db
from app.models import base_model


class Carrier(base_model.BaseModel):
    '''
    Clase empresa de telecomunicaciones.
    name: Nombre de la empresa (Claro, Entel, etc.)
    '''
    __tablename__ = 'carriers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    mcc = db.Column(db.Integer)
    mnc = db.Column(db.Integer)
    sims = db.relationship('Sim', backref='carrier', lazy='dynamic')
    telephony_observation_events = db.relationship('TelephonyObservationEvent', backref='carrier', lazy='dynamic')

    def __init__(self, name=None, mcc=None, mnc=None):
        self.name = name
        self.mcc = mcc
        self.mnc = mnc

    def __repr__(self):
        return '<Telco %r>' % (self.name)
