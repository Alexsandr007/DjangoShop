from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from blog.models import Blog
from django.urls import reverse

class BlogView(ListView):
    model = Blog
    paginate_by = 5
    context_object_name = 'blog_list'
    template_name = "blog/blog.html"

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})

class BlogDetailView(DetailView):
    model = Blog
    pk_url_kwarg = 'blog_id'
    template_name = "blog/blog-detail.html"
