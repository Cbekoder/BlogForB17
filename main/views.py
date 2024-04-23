from django.db.models.functions import ExtractYear, ExtractMonth
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'home.html')

def blog(request):
    blog_posts = Blog.objects.annotate(year=ExtractYear('date'), month=ExtractMonth('date')).order_by('-date')

    grouped_posts = {}
    for post in blog_posts:
        year_month = (post.year, post.month)
        if year_month not in grouped_posts:
            grouped_posts[year_month] = []
        grouped_posts[year_month].append(post)
    return render(request, 'blog.html', {'grouped_posts': grouped_posts})