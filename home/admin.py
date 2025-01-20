from django.contrib import admin
from .models import Service, ProjectCategory, Project, Work, Skill

admin.site.register(Service)
admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(Work)
admin.site.register(Skill)