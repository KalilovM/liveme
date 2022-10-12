from django.db.models import Q
import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='title_desc_filter', label="search")

    category = django_filters.CharFilter(lookup_expr="exact", field_name="category__title")

    class Meta:
        model = Product
        fields = [
            "search",
            "category"
        ]
        
    def title_desc_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title_en__iregex=value) | Q(title_ru__iregex=value) | Q(title_kg__iregex=value) | Q(title_tr__iregex=value) |
             Q(description_en__iregex=value) | Q(description_ru__iregex=value) | Q(description_kg__iregex=value) | Q(description_tr__iregex=value)
        )
