from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer, SerializerMetaclass
from resumeapp import models
from rest_framework.views import APIView
from resumeapp import serializers
from resumeapp.serializers import CompanySerializer, ProfileSerializer, ProjectSerializer, ContactSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework import generics,status, exceptions


@swagger_auto_schema(tags=['Work experience API'])
class ExperienceAPIView(APIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = models.Company.objects.all()
        ser = self.serializer_class(qs, many=True)
        json_data =  JSONRenderer().render(ser.data)       
        return HttpResponse(json_data, content_type='application/json')


@swagger_auto_schema(tags=['Education API'])
class ProfileAPIView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        qs = models.Profile.objects.all()
        ser = self.serializer_class(qs, many=True)
        json_data =  JSONRenderer().render(ser.data)      
        return HttpResponse(json_data, content_type='application/json')


@swagger_auto_schema(tags=['Projects API'])
class ProjectAPIView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        qs = models.Project.objects.all()
        ser = self.serializer_class(qs, many=True)
        json_data =  JSONRenderer().render(ser.data)      
        return HttpResponse(json_data, content_type='application/json')


@swagger_auto_schema(tags=['Contact API'])
class ContactAPIView(generics.GenericAPIView):
    serializer_class = ContactSerializer
    permission_classes = []
    def post(self, request):
        print("ojf", request.data)
        serializer = self.serializer_class(data=request.data)
        return Response({'message':'success'})