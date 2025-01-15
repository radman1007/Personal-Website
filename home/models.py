from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(100)

    def __str__(self):
        return self.name


class Project(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    body = models.TextField()
    category = models.ManyToManyField(ProjectCategory, related_name='category')
    customer = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.title