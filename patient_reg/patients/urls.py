from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^register/', views.register, name='api_register'),
]