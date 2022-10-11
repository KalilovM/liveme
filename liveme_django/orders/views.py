from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order
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
