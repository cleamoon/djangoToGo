# Within "python manage.py shell"

from polls.models import Project

project1 = Project(name="Full Stack Development", desc="Most popular project", is_good=True)
project1.save()
project2 = Project(name="Delete Legacy Code", desc="Very dangerous project", is_good=False)
project2.save()
project3 = Project(name="Java Distributed Deveopment", desc="Complex distributed project", is_good=True)
project3.save()

project = Project.objects.get(id=3)
print(project.name)
project.delete()
project = Project.objects.get(id=1)
project.name = 'Python Full Stack Development'
project.save()


import random
for i in range(0, 10):
    Project(name="Random project" + str(i), desc="Random tasks", is_good=bool(random.getrandbits(1))).save()
Project.objects.all()
Project.objects.filter(name="Python Full Stack Development")
Project.objects.filter(name__contains="Full Stack")
Project.objects.filter(name__startswith="Python")
Project.objects.filter(name__endswith="Python")
Project.objects.filter(is_good=True)
Project.objects.filter(is_good=True, name__contains="Python")
Project.objects.filter(is_good=True).filter(name__contains="Python")
Project.objects.filter(id__lt=8)
Project.objects.filter(id__gt=2)
Project.objects.filter(id__range=(3, 7))
Project.objects.get(id=1).name

Project.objects.order_by('id')
Project.objects.order_by('-id')


from polls.models import Manager
Manager(name="Alice", desc="Manager 1", gender=False, birthday="2000-01-01", photo="./photo/Alice.jpg", gcount=1, bcount=2, proj_id="1").save()
Manager.objects.filter(proj_id__id="1")
Project.objects.get(pk=1).manager_set.all().first().name
Manager.objects.filter(proj_id__name__contains="Full Stack")