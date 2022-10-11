from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        if self.context["request"].user.is_authenticated:
            user = self.context["request"].user
            order = Order.objects.create(**validated_data)
            user.orders.add(order)
        else:
            order = Order.objects.create(**validated_data)
        return order
