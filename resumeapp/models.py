from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    projects = models.ManyToManyField(Project, related_name='projects', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Profile(models.Model):
    language = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    hobbies = ArrayField(models.CharField(max_length=10, blank=True))

    def __str__(self):
        return self.language

class Employer(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name