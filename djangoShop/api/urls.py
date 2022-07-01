from django.urls import path

from . import views
# from django.views.generic import TemplateView

app_name = 'api'
urlpatterns = [
    path('products/', views.color_size_sort, name='color_size_sort'),
    path('bag/', views.bag, name='bag'),
    path('card_content/', views.card_content, name='card_content')
]