from django.db import models


class Service(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    body = models.TextField()
    number = models.CharField(max_length=3)
    
    def __str__(self):
        return self.title


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    body = models.TextField()
    category = models.ManyToManyField(ProjectCategory, related_name='category')
    customer = models.CharField(max_length=100, null=True, blank=True)
    link =  models.CharField(max_length=250)
    
    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    loc = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
   

class Skill(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name