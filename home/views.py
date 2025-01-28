from django.shortcuts import render
from .models import *
from blog.models import Blog

def home(request):
    services = Service.objects.all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    works = Work.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    customer = Contact.objects.all()
    blogs = Blog.objects.all()
    if request.method == "POST":
        contact = Contact(request.POST)
        if contact.is_valid():
            contact.save()
    context = {
        'services' : services,
        'project_categories' : project_categories,
        'projects' : projects,
        'works' : works,
        'educations' : educations,
        'skills' : skills,
        'blogs' : blogs,
    }
    return render(request, 'index.html', context)