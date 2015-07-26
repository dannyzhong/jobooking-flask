from app import db
from sqlalchemy.orm import backref
from app.common.models import Base


class Timetable(Base):
    __tablename__ = "timetable"
    start_time = db.column(db.DateTime)
    end_time = db.column(db.DateTime)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    
    
    def __init__(self, start_time, end_time, job):
        self.start_time = start_time
        self.end_time = end_time
        self.job = job
        
      
    
    


