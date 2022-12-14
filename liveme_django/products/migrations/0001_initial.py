# Generated by Django 4.1.1 on 2022-09-28 14:51

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=100,
                        null=True,
                        populate_from=["title"],
                        unique=True,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="category/%Y/%m/%d/"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("is_published", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=50, null=True)),
                ("title_en", models.CharField(blank=True, max_length=50, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=50, null=True)),
                ("title_kg", models.CharField(blank=True, max_length=50, null=True)),
                ("title_tr", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=100,
                        null=True,
                        populate_from=["title"],
                        unique=True,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="category/%Y/%m/%d/"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("is_published", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100)),
                ("title_en", models.CharField(blank=True, max_length=100, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=100, null=True)),
                ("title_kg", models.CharField(blank=True, max_length=100, null=True)),
                ("title_tr", models.CharField(blank=True, max_length=100, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("description_en", models.TextField(blank=True, null=True)),
                ("description_ru", models.TextField(blank=True, null=True)),
                ("description_kg", models.TextField(blank=True, null=True)),
                ("description_tr", models.TextField(blank=True, null=True)),
                (
                    "cover",
                    models.ImageField(upload_to="product_gallary/covers/%Y/%m/%d/"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=200,
                        populate_from=["title"],
                        unique=True,
                    ),
                ),
                ("regular_price", models.FloatField(blank=True, null=True)),
                ("sale_price", models.FloatField(blank=True, null=True)),
                ("stock", models.IntegerField(blank=True, default=0, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("is_published", models.BooleanField(default=True)),
                (
                    "brand",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.brand",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="product_gallary/%Y/%m/%d/"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="images",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
