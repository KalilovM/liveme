from cgitb import lookup
import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="iregex", field_name="title")
    description = django_filters.CharFilter(
        lookup_expr="exact", field_name="description__title"
    )
    category = django_filters.CharFilter(lookup_expr="exact", field_name="category__title")

    class Meta:
        model = Product
        fields = [
            "title",
            "title_en",
            "title_ru",
            "title_kg",
            "title_tr",
            "description",
            "description_ru",
            "description_kg",
            "description_en",
            "description_tr",
        ]
