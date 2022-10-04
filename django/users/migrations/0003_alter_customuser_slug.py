# Generated by Django 4.1.1 on 2022-09-16 16:50

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_customuser_is_admin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                max_length=200,
                populate_from=["username"],
                unique=True,
            ),
        ),
    ]
