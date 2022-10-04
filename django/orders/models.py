from django.db import models


class Order(models.Model):
    client_email = models.CharField(max_length=60, blank=True, null=True)
    client_address = models.CharField(max_length=255, blank=False, null=False)
    client_phone = models.CharField(max_length=60, blank=False, null=False)
    client_name = models.CharField(max_length=60, blank=False, null=False)
    choice = (
        ("Наличкой", "Наличкой"),
        ("Банковский счет", "Банковский счет"),
        ("Картой", "Картой"),
    )
    products = models.JSONField(encoder=None, decoder=None, blank=True, null=True)
    payment_method = models.CharField(max_length=100, choices=choice)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.created}"
