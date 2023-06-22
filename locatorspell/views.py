from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from blog.models import Blog

def index(request):
  blog_posts = Blog.objects.order_by('date_posted')
  context = { "blog_posts": blog_posts }
  return render(request, "index.html", context)

def about(request):
  return render(request, "about.html")