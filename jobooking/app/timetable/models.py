from app import db
from sqlalchemy.orm import backref
from app.common.models import Base


class Timetable(Base):
    __tablename__ = "timetable"
    ant_id = db.Column(db.Integer, db.ForeignKey('ant.id'))
    ant = db.relationship("Ant", backref=backref("Timetable", uselist=False))  
    timeslots = db.relationship("Timeslot", backref="timetable")
        
    def __init__(self, start_time, end_time, job):
        self.start_time = start_time
        self.end_time = end_time
        self.job = job
        
      
class Timeslot(Base):
    __tablename__ = "timeslot"
    timetable_id = db.Column(db.Integer, db.ForeignKey('timetable.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    job = db.relationship("Job", backref=backref("Timeslot", uselist=False))
    start_time = db.column(db.DateTime)
    end_time = db.column(db.DateTime)
        
    
    


