from app.category.models import Category, Category_Image
from app.job.models import Job,Job_Image
from app.nest.models import Nest
from app import db




nest1 = Nest("nest1")
nest2 = Nest("nest2")

image1 = Category_Image("image_path1")
image2 = Category_Image("image_path2")
image3 = Category_Image("image_path3")
image4 = Category_Image("image_path4")
category1 = Category("nail", "i love nails",image1,10)
category2 = Category("eyebrow", "i hate eyebrow",image2,22)
category3 = Category("eyebrow 2", "i hate eyebrow too",image3)
category4 = Category("eyebrow 4", "i hate eyebrow too four",image2)


jobimage1 = Job_Image("jobimage_path1")
jobimage2 = Job_Image("jobimage_path2")
jobimage3 = Job_Image("jobimage_path3")
jobimage4 = Job_Image("jobimage_path4")
jobimage5 = Job_Image("jobimage_path5")


job1 = Job("job1 title","job1 desc",category1,jobimage1,nest1)
job2 = Job("job2 title","job2 desc",category2,jobimage2,nest1)
job3 = Job("job3 title","job3 desc",category3,jobimage3,nest2)
job4 = Job("job4 title","job4 desc",category2,jobimage4,nest2)



db.session.add(nest1)
db.session.add(nest2)


db.session.add(image1)
db.session.add(image2)
db.session.add(image3)
db.session.add(image4)

db.session.add(jobimage1)
db.session.add(jobimage2)
db.session.add(jobimage3)
db.session.add(jobimage4)
db.session.add(jobimage5)

db.session.add(category1)
db.session.add(category2)
db.session.add(category3)
db.session.add(category4)

db.session.add(job1);
db.session.add(job2);
db.session.add(job3);
db.session.add(job4);







db.session.commit()
