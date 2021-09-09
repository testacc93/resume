from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from resumeapp import urls
from resumeapp import views

urlpatterns = [
    path('work-experience', views.ExperienceAPIView.as_view(), name='work-experience'),
    # path('profile', views.ProfileAPIView.as_view(), name='profile'),
    path('projects', views.ProjectAPIView.as_view(), name='project'),
    # path('contact-me', views.ContactAPIView.as_view(), name='contact'),
    path('interested-employer', views.EmployerAPIView.as_view(), name='employer'),
    path('delete-interested-employer/<id>', views.DestroyEmployerAPIView.as_view(), name='intri-employer'),
    path('all-interested-employer', views.IntriEmployerAPIView.as_view(), name='employer'),
]
