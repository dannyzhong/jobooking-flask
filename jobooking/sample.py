from app.job.models import Job, Job_Image
from app.nest.models import Nest
from app.category.models import Category
from app import db


nest1 = Nest("test_nest1")
nest2 = Nest("test_nest2")

job1 = Job("job1","job1",nest1)
job2 = Job("job2","job2",nest1)
job3 = Job("job3","job3",nest2)

image1 = Job_Image("image_path1",job1)
image2 = Job_Image("image_path2",job1)
image3 = Job_Image("image_path3",job1)
image4 = Job_Image("image_path4",job1)
image5 = Job_Image("image_path5",job1)
image6 = Job_Image("image_path6",job2)
image7 = Job_Image("image_path7",job2)
image8 = Job_Image("image_path8",job3)

category1 = Category("nail", "i love nails")
category2 = Category("eyebrow", "i hate eyebrow")

db.session.add(nest1)
db.session.add(nest2)
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

db.session.add(category1)
db.session.add(category2)

db.session.commit()

