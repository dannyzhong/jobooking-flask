from app.job.models import Job, Image
from app.jobookee.models import Jobookee
from app import db


jobookee1 = Jobookee("test_jobookee1")

jobookee2 = Jobookee("test_jobookee2")


job1 = Job("job1","job1",jobookee1)
job2 = Job("job2","job2",jobookee1)

job3 = Job("job3","job3",jobookee2)

image1 = Image("image_path1",job1)
image2 = Image("image_path2",job1)
image3 = Image("image_path3",job1)
image4 = Image("image_path4",job1)
image5 = Image("image_path5",job1)

image6 = Image("image_path6",job2)
image7 = Image("image_path7",job2)
image8 = Image("image_path8",job3)


db.session.add(jobookee1)
db.session.add(jobookee2)
db.session.add(job1)
db.session.add(job2)
db.session.add(job3)

db.session.add(image1)
db.session.add(image2)
db.session.add(image3)
db.session.add(image4)
db.session.add(image5)
db.session.add(image6)
db.session.add(image7)
db.session.add(image8)

db.session.commit()

