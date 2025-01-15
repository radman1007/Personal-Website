from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title