from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.ProductView.as_view(), name='product_catalog'),
    path('product_detail/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/sort/', views.FilterProductView.as_view(), name='product_sorting'),
]

