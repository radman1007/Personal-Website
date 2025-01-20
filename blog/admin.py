from django.contrib import admin
from .models import BlogCategory, Blog

admin.site.register(BlogCategory)
admin.site.register(Blog)