from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Blog

# Create your views here.
def index(request):
  blog_list = Blog.objects.order_by("-date_posted")[:5]
  context = {"blog_list": blog_list}
  return render(request, "blog/index.html", context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail.html", {"blog": blog})