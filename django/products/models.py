from django.db import models
from django_extensions.db.fields import AutoSlugField
from decouple import config

alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "j",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ы": "i",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}


class ProductImage(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="images",
    )
    image = models.ImageField(
        upload_to="product_gallary/%Y/%m/%d/", null=True, blank=True
    )

    def __str__(self):
        return f'{config("DOMAIN")}/media/{self.image}'


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(upload_to="product_gallary/covers/%Y/%m/%d/")
    slug = AutoSlugField(
        populate_from=["title"], max_length=200, unique=True, blank=True
    )
    regular_price = models.FloatField(null=True, blank=True)
    sale_price = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(default=0, null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, null=True, blank=True
    )
    brand = models.ForeignKey("Brand", on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} {self.title}"

    def get_name(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    slug = AutoSlugField(
        populate_from=["title"], max_length=100, unique=True, null=True
    )
    image = models.ImageField(upload_to="category/%Y/%m/%d/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(
        populate_from=["title"], max_length=100, unique=True, null=True
    )
    image = models.ImageField(upload_to="category/%Y/%m/%d/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
