from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from resumeapp import urls
from resumeapp import views

urlpatterns = [
    path('work-experience', views.ExperienceAPIView.as_view(), name='work-experience'),
    path('profile', views.ProfileAPIView.as_view(), name='profile'),
    path('projects', views.ProjectAPIView.as_view(), name='project'),
    # path('contact', views.ContactAPIView.as_view(), name='contact'),
]