# Generated by Django 5.0.1 on 2024-02-16 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0029_alter_reviewrating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
