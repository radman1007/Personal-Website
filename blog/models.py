from django.db import models
from django.urls import reverse


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.CharField(max_length=100)
    category = models.ManyToManyField(BlogCategory, related_name='blogs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("blog_detail", args=[self.id])
    
    def __str__(self):
        return self.title