from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from rest_framework import permissions
from rest_framework import viewsets


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_permissions(self):

        if self.action == "create":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        serializer = OrderSerializer(data=request.data)
        if self.request.user.is_authenticated:
            if serializer.is_valid():
                order = Order.objects.create(serializer.validated_data)
                user.orders.add(order)
        else:
            order = Order.objects.create(serializer.validated_data)
        return order


class OrderItemView(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.all().select_related("product", "order")
