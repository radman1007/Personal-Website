from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog' : blog
    }
    return render(request, 'blog-detail.html', context)