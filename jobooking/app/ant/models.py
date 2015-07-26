from app import db
from sqlalchemy.orm import backref
from app.common.models import Base


class Ant(Base):
    __tablename__ = "ant"
    first_name = db.Column(db.String(128),  nullable=False)
    last_name = db.Column(db.String(128),  nullable=False)
    gender = db.Column(db.Text,nullable=True)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'))
    timetables = db.relationship('Timetable', backref='ant', lazy='dynamic')
    jobs = db.relationship('Timetable', backref='ant', lazy='dynamic')
    
    
    
    def __init__(self, first_name,last_name, gender, nest):

        self.first_name     = first_name
        self.last_name = last_name
        self.gender = gender
        self.nest = nest
        
        
class Ant_Job(Base):
    __tablename__ = "antjob"
    ant_id = db.Column(db.Integer, db.ForeignKey('ant.id'))
    