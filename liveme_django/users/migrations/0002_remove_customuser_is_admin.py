# Generated by Django 4.1.1 on 2022-09-15 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="is_admin",
        ),
    ]
