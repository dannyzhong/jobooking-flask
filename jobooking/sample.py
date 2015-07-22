from app.job.models import Job
from app.jobookee.models import Jobookee
from app import db


jobookee1 = Jobookee("test_jobookee1")

jobookee2 = Jobookee("test_jobookee2")


job1 = Job("job1","job1",jobookee1)
job2 = Job("job2","job2",jobookee1)

job3 = Job("job3","job3",jobookee2)
db.session.add(jobookee1)
db.session.add(jobookee2)
db.session.add(job1)
db.session.add(job2)
db.session.add(job3)
db.session.commit()

print jobookee1.jobs.all()
