from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'card'
urlpatterns = [

    # path('', TemplateView.as_view(template_name="card/card.html"), name='card_detail'),
    path('', views.cart_detail, name='card_detail'),
    path('add/<int:product_id>/',
         views.cart_add,
         name='card_add'),
    path('remove/<int:product_id>/',
         views.cart_remove,
         name='card_remove'),
    path('order/<str:user_email>/',
         views.send,
         name='card_order'),
]