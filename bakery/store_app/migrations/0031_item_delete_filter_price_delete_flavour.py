# Generated by Django 5.0.1 on 2024-02-16 07:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0030_remove_reviewrating_item_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('image', models.ImageField(upload_to='Item_images/img')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('information', models.TextField()),
                ('description', models.TextField()),
                ('stock', models.CharField(choices=[('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK')], max_length=200)),
                ('ingredients', models.CharField(choices=[('WITH EGG', 'WITH EGG'), ('WITHOUT EGG', 'WITHOUT EGG')], max_length=200)),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.categories')),
            ],
        ),
        migrations.DeleteModel(
            name='Filter_Price',
        ),
        migrations.DeleteModel(
            name='Flavour',
        ),
    ]
