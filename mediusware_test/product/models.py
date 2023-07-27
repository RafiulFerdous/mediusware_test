from django.db import models

from django.conf import settings
import os

# Create your models here.

def get_image_upload_path(instance, filename):
    return os.path.join('product_images', str(instance.product.id), filename)



class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=225)
    sku = models.CharField(max_length=225)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.ImageField(upload_to=get_image_upload_path)
    thumbnail = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product Image {self.id}"


class Variant(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductVariant(models.Model):
    id = models.BigAutoField(primary_key=True)
    variant_id = models.ForeignKey(Variant, on_delete=models.CASCADE)

    product_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product Variant {self.id}"



class ProductVariantPrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    price = models.CharField(max_length=225)
    stock = models.CharField(max_length=225)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # New ForeignKey field for Product
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product Variant Price {self.id}"


