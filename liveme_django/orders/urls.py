from django.urls import path
from .views import OrderView, OrderItemView

urlpatterns = [
    path("", OrderView.as_view({"post": "create", "get": "list"}), name="order_list"),
    path(
        "<int:pk>",
        OrderView.as_view({"put": "update", "delete": "destroy"}),
        name="orders",
    ),
    path("item/", OrderItemView.as_view({"post": "create", "get": "list"}), name="order_list"),
    path(
        "item/<int:pk>",
        OrderItemView.as_view({"put": "update", "delete": "destroy"}),
        name="orders",
    ),
]
