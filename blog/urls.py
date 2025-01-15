from django.urls import path
from .views import blog_detail

urlpatterns = [
    path('blog-detail/<int:pk>', blog_detail, name='blog_detail'),
]
