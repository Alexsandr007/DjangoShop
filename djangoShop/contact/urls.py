from django.urls import path

from . import views

urlpatterns = [
    path('', views.TemplateView.as_view(template_name="contact/contact.html"), name='contact'),
]