# Generated by Django 5.0.3 on 2024-07-04 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0102_alter_profile_address_alter_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]
