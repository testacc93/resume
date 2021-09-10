from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer, SerializerMetaclass
from rest_framework.utils import json
from resumeapp import models
from rest_framework.views import APIView
from resumeapp import serializers
from resumeapp.serializers import CompanySerializer, IntriEmployeeSerializer, ProfileSerializer, ProjectSerializer, ContactSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework import generics,status, exceptions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView


@swagger_auto_schema(tags=['Work experience API'])
class ExperienceAPIView(APIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = models.Company.objects.all()
        # breakpoint()
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
        

class EmployerAPIView(generics.GenericAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = []
    authentication_classes = []

    @swagger_auto_schema(tags=['Generate interested employer'])
    def post(self, request, **employer):
        data = request.data
        models.Employer.objects.create(name=data['name'], company_name=data['company_name'])
        id = models.Employer.objects.filter(name=data['name']).values('id')
        id_list = []
        for item in id:
            id_list.append(item)
        return Response({'message':'Thank you for testing post method. Incase you wish to test delete method, id: {}'.format(item['id'])}, status=201)


class IntriEmployerAPIView(APIView):
    serializer_class = IntriEmployeeSerializer

    @swagger_auto_schema(tags=['List all interested employers'])
    def get(self, request):
        qs = models.Employer.objects.all()
        ser = self.serializer_class(qs, many=True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json')


class DestroyEmployerAPIView(DestroyAPIView):
    
    @swagger_auto_schema(tags=['Delete interested employer'])
    def delete(self, request, id):
        obj = models.Employer.objects.filter(id=id)
        if len(obj)==0:
            return Response({'message':'Employer not found'}, status=400)
        models.Employer.objects.filter(id=id).delete()
        return Response({'message':'Employer deleted successfully'})


