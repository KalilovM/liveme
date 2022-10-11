from .models import Product, Category
from modeltranslation.translator import translator, TranslationOptions


class ProductTranslation(TranslationOptions):
    fields = ("title", "description")


translator.register(Product, ProductTranslation)


class CategoryTranslation(TranslationOptions):
    fields = ("title",)


translator.register(Category, CategoryTranslation)
