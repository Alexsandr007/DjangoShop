from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', TemplateView.as_view(template_name="base/about.html"), name='about'),
]