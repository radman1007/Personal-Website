from django.shortcuts import render

def blog_detail(request):
    return render(request, 'blog-detail.html')