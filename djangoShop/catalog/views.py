from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from blog.models import Product
# Create your views here.
class ProductView(ListView):
    model = Product
    paginate_by = 5

class ProductDetailView(DetailView):
    model = Product
