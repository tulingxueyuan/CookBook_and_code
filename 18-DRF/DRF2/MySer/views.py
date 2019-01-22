from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.
from MySer.models import *
from rest_framework.response import  Response
from MySer.serializers import *

from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet

class StudentGenAPIView(GenericAPIView):
    queryset =  Student.objects.all()
    serializer_class =  StudentSerializer


    def get(self, request):
        ser = self.get_serializer(self.queryset.all(), many=True)
        # ser = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=ser.data)



class StudentVS(viewsets.ModelViewSet):
    pass

class StudentAPIView(APIView):
    '''
    处理用户的get请求
    '''
    def get(self, request):
        '''
        处理业务
        跟数据库交互
        :param request:
        :return:
        '''
        stus = Student.objects.all()
        ser = StudentSerializer(stus, many=True)
        return Response(data=ser.data)


from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):

        print("hahhahahahah ")
        rst = super(StudentViewSet, self).list(*args, **kwargs)
        return rst

