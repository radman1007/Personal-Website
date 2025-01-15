from django.shortcuts import render
from .models import *
from blog.models import Blog

def home(request):
    services = Service.objects.all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    works = Work.objects.all()
    skills = Skill.objects.all()
    blogs = Blog.objects.all()
    context = {
        'services' : services,
        'project_categories' : project_categories,
        'projects' : projects,
        'works' : works,
        'skills' : skills,
        'blogs' : blogs,
    }
    return render(request, 'index.html', context)