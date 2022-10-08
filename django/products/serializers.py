from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Category
        fields = (
            "title",
            "title_ru",
            "image",
            "created",
            "updated",
            "is_published",
        )


class BrandSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Brand
        fields = ("title", "image", "created", "updated", "is_published")



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)
        

class ProductSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=False, many=False, queryset=Category.objects.all())

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
            "regular_price",
            "sale_price",
            "stock",
            "category",
            "created",
            "updated",
            "is_published",
            "slug",
        )
        
        


class SingleProductSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=False, many=False, queryset=Category.objects.all())
    images = ProductImageSerializer(many=True)

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
