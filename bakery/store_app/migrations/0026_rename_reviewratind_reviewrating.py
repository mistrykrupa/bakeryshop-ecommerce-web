# Generated by Django 5.0.1 on 2024-02-15 10:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0025_reviewratind'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviewRatind',
            new_name='ReviewRating',
        ),
    ]
