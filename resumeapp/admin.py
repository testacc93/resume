from django.contrib import admin
from resumeapp.models import Project, Company, Profile
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']

admin.site.register(Company, CompanyAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']

admin.site.register(Project, ProjectAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['language', 'address', 'hobbies']

admin.site.register(Profile, ProfileAdmin)