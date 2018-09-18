from django.db import models

# Create your models here.

class Teacher(models.Model):

    name = models.CharField(max_length=12)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)

    def __str__(self):
        return  self.name

class Studenty(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    myteacher = models.ForeignKey(Teacher )



