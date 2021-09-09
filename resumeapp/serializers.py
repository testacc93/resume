from django.utils import tree
from rest_framework import serializers
from resumeapp.models import Company, Employer, Project, Profile

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'start_date', 'end_date', 'projects']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['language', 'address', 'hobbies']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'company']


class ContactSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    email = serializers.CharField(required=True)


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    company_name = serializers.CharField(required=True)


class IntriEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['name', 'company_name']

