# Generated by Django 4.1.1 on 2022-09-15 22:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="client_address",
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="client_email",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="client_name",
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="client_phone",
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
