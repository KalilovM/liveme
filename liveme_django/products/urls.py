from django.urls import path
from .views import ProductView, ProductImageView, CategoryView, BrandView

urlpatterns = [
    path("", ProductView.as_view({"get": "list", "post": "create"}), name="products"),
    path(
        "<int:pk>",
        ProductView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="products",
    ),
    path(
        "image/",
        ProductImageView.as_view({"get": "list", "post": "create"}),
        name="productsimage",
    ),
    path(
        "image/<int:pk>",
        ProductImageView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="productsimage",
    ),
    path(
        "category/",
        CategoryView.as_view({"get": "list", "post": "create"}),
        name="category",
    ),
    path(
        "category/<int:pk>",
        CategoryView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="categoryview",
    ),
    path("brand/", BrandView.as_view({"get": "list", "post": "create"})),
    path(
        "brand/<int:pk>",
        BrandView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
]
