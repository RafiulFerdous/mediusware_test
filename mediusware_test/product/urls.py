from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for your Django views
    path('/', views.react_app, name='react_app'),
]