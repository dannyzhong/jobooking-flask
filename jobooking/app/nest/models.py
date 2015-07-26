from app import db
from sqlalchemy.orm import backref
from app.common.models import Base

    
class Nest(Base):
    __tablename__ = "nest"
    name = db.Column(db.String(128),  nullable=False)
    jobs = db.relationship('Job', backref='jobookee',lazy='dynamic')
    ants = db.relationship('Ant', backref='jobookee',lazy='dynamic')

    def __init__(self, name):

        self.name     = name
        
        

    def __repr__(self):
        return '<Nest Name %r>' % (self.name)          