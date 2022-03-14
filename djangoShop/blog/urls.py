from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog_catalog'),
    path('blog_detail/<int:blog_id>/', views.BlogDetailView.as_view(), name='blog_detail'),
]