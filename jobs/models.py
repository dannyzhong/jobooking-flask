from jobs import db


class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())



class jobs(Base):
    __tablename__ = "jobs"
    job_title = db.Column(db.String(128),  nullable=False)


    def __init__(self, job_title):

        self.job_title     = job_title


    def __repr__(self):
        return '<Title %r>' % (self.job_title)                        
