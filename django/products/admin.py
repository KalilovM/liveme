from django.contrib import admin
from .models import ProductImage, Brand, Category, Product


class ProductImageInline(admin.TabularInline):
    fields = ("image",)
    model = ProductImage


def dublicate_obj(modeladmin, request, queryset):
    # клонирование выбранных obj
    for obj in queryset:
        obj.pk = None
        obj.save()


dublicate_obj.short_description = "Дублировать объект"


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "regular_price",
        "sale_price",
        "stock",
        "category",
        "is_published",
    )
    inlines = [
        ProductImageInline,
    ]
    actions = [dublicate_obj]


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)
