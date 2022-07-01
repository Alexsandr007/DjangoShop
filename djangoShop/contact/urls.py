from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'contact'
urlpatterns = [
    path('', TemplateView.as_view(template_name="contact/contact.html"), name='contact_page'),
]