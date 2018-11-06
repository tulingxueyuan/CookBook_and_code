from django.db import models

# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=200)
    className = models.CharField(max_length=20)

    def showName(self):
        return "hahahahah"

    showName.short_description = "显示名称"
    showName.admin_order_field = 'loc'

    def __str__(self):
        return self.className

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    cource = models.CharField(max_length=20)

    classroom = models.OneToOneField(ClassRoom)

    def roomloc(self):
        return self.classroom.loc

    roomloc.short_description = "地点"



    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    classroom = models.ForeignKey(ClassRoom)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name
