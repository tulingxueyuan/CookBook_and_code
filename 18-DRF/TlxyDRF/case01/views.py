from django.shortcuts import render
from rest_framework import viewsets
from case01.serializers import *
from case01.models import Student
# Create your views here.


class StudentVS(viewsets.ModelViewSet):
    serializer_class =  StudentSer
    queryset = Student.objects.all()


