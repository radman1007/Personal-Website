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
    link =  models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    loc = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title


class Education(models.Model):
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


class Story(models.Model):
    image = models.ImageField()
    logo = models.ImageField()
    body = models.TextField()
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    text = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.f_name} {self.l_name} : {self.service}"
