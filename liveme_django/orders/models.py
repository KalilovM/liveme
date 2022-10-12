from django.db import models
from products.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True, blank=True)
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.order.client_name}"


class Order(models.Model):
    choice = (
        ("Наличкой", "Наличкой"),
        ("Банковский счет", "Банковский счет"),
        ("Картой", "Картой"),
    )
    statuses = (
        ("Обрабатывается", "Обрабатывается"),
        ("Подтверждено", "Подтвержденго"),
        ("Успешно", "Успешно"),
        ("Откланено", "Откланено"),
    )
    client_email = models.CharField(max_length=60, blank=True, null=True)
    client_address = models.CharField(max_length=255, blank=False, null=False)
    client_phone = models.CharField(max_length=60, blank=False, null=False)
    client_name = models.CharField(max_length=60, blank=False, null=False)
    payment_method = models.CharField(max_length=100, choices=choice)
    order_status = models.CharField(max_length=100,choices=statuses, default="Обрабатывается")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client_name}"
