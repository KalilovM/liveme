from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    count = serializers.IntegerField()     
    class Meta:
        model = Category
        fields = (
            "title",
            "image",
            "updated",
            "created",
            "is_published",
            "count"
        )


class BrandSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Brand
        fields = ("title", "image","updated","created","is_published",)



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "cover",
            "regular_price",
            "sale_price",
            "is_published",
            "slug",
        )
        
        


class SingleProductSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    images = ProductImageSerializer(many=True)
    category = serializers.CharField(source='category.title')
    brand = serializers.CharField(source='brand.title')

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "title_ru",
            "description",
            "description_ru",
            "cover",
            "brand",
            "images",
            "regular_price",
            "sale_price",
            "stock",
            "category",
            "created",
            "updated",
            "is_published",
            "slug",
        )
