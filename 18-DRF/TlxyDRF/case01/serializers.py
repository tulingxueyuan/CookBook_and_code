from rest_framework import serializers

from case01.models import *

class StudentSer(serializers.ModelSerializer):
    class Meta:
        model =  Student
        fields = '__all__'
