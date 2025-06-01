from django.shortcuts import render
from .models import *
from blog.models import Blog

def home(request):
    careerstats = CareerStat.objects.all().last()
    services = Service.objects.all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    works = Work.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    stories = Story.objects.all()
    blogs = Blog.objects.all()
    if request.method == "POST":
        contact = Contact(request.POST)
        if contact.is_valid():
            contact.save()
    context = {
        'careerstats' : careerstats,
        'services' : services,
        'project_categories' : project_categories,
        'projects' : projects,
        'works' : works,
        'educations' : educations,
        'skills' : skills,
        'stories' : stories,
        'blogs' : blogs,
    }
    return render(request, 'index.html', context)