# Generated by Django 5.0.1 on 2024-02-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0039_rename_username_order_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
