# Generated by Django 5.0.1 on 2024-02-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0081_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
