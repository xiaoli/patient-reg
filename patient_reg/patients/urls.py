from django.urls import path
from . import views

urlpatterns = [
    path(r'^register/', views.register, name='api_register'),
]