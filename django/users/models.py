from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.fields import AutoSlugField


class CustomUser(AbstractUser):
    adress = models.CharField(max_length=200, blank=True, null=True)
    orders = models.ManyToManyField("orders.Order", blank=True, null=True)
    slug = AutoSlugField(
        populate_from=["username"], max_length=200, unique=True, blank=True
    )

    def __str__(self):
        return f"{self.id} {self.username}"
