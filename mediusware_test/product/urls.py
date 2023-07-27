from django.contrib import admin
from django.urls import path
from product.views import ProductViewset

urlpatterns = [
    path('product', ProductViewset.as_view({
        'get': 'list',
        'post': 'create',
        'post': 'retrieve',
    }))]