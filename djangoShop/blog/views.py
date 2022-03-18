from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from blog.models import Blog

class BlogView(ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog
