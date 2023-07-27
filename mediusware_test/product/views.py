from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .ProductSerializer import ProductSerializer


# Create your views here.

class ProductViewset(viewsets.ViewSet):
    def list(self, request):
        products= Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request):
        query_params = request.query_params

        title = query_params.get('title', None)
        variant = query_params.get('variant', None)
        price = query_params.get('price', None)
        start_date = query_params.get('start_date', None)
        end_date = query_params.get('end_date', None)

        queryset = Product.objects.all()

        if title:
            queryset = queryset.filter(title__icontains=title)

        if variant:
            queryset = queryset.filter(variants__variant__title__icontains=variant)

        if price:
            queryset = queryset.filter(variants__prices__price=price)

        if start_date and end_date:
            queryset = queryset.filter(created_at__range=[start_date, end_date])

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
