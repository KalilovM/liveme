import django_filters
from rest_framework import permissions
from rest_framework import viewsets
from .serializers import (
    ProductSerializer,
    ProductImageSerializer,
    SingleProductSerializer,
    CategorySerializer,
    BrandSerializer,
)
from .filters import ProductFilter
from .models import Product, ProductImage, Category, Brand
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count


class LargeResultsSetPagination(PageNumberPagination):
    page_size = None
    page_size_query_param = "page_size"


class ProductView(viewsets.ModelViewSet):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = (
        "title",
        "title_ru",
        "title_kg",
        "title_en",
        "title_tr",
        "category__title",
    )
    pagination_class = LargeResultsSetPagination

    def get_permissions(self):
        permission_classes = [permissions.AllowAny]
        if self.action == ["update", "destroy", "create"]:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = ProductSerializer
        if self.action == "retrieve":
            serializer_class = SingleProductSerializer
        return serializer_class

    def get_queryset(self):
        return Product.objects.all().prefetch_related('category','brand')


class ProductImageView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.prefetch_related('images').values('image')


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all().annotate(count=Count('products'))
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
