from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='product_catalog'),
    path('product_detail/<int:product_id>/', views.ProductView.as_view(), name='product_detail'),
]