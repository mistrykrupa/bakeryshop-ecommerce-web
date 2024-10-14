# Generated by Django 5.0.1 on 2024-02-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0031_item_delete_filter_price_delete_flavour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(choices=[('200 To 500', '200 To 500'), ('500 To 1000', '500 To 1000'), ('1000 To 1500', '1000 To 1500'), ('1500 To 2000', '1500 To 2000')], max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
