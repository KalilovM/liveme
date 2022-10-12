from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'client_email', 'client_phone','order_status']


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'product_count']
