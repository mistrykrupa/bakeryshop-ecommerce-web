# Generated by Django 5.0.1 on 2024-01-21 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_images_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flavour',
            new_name='Subcategories',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Flavour',
            new_name='Subcategories',
        ),
    ]
