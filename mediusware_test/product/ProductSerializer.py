from rest_framework import serializers

from .models import Product,ProductImage
from django.db import transaction


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product_images_data = validated_data.pop('product_images', [])

        with transaction.atomic():

            product = Product.objects.create(**validated_data)


            for product_image_data in product_images_data:
                ProductImage.objects.create(product=product, **product_image_data)

        return product