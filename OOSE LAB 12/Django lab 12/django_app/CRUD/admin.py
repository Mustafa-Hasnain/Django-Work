from django.contrib import admin

# Register your models here.
from .models import Project, Students

admin.site.register(Project)
admin.site.register(Students)