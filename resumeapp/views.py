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
        data = request.data
        print("ojf", request.data)
        message = data['message']
        email = data['email']
        if len(message) < 10:
            if '@' not in email and '.com' not in email:
                return Response({'message':'doesnt look like a valid email'})
            return Response({'message':'Please describe concern in detail'})

        if len(message) in range(10, 50):
            if '@' not in email and '.com' not in email:
                return Response({'message':'doesnt look like a valid email'})
            return Response({'message':'good try!, more details would be of help to me'})
        else:
            if '@' not in email and '.com' not in email:
                return Response({'message':'doesnt look like a valid email'})
            return Response({'message':'Okay! I will look into it'})
        