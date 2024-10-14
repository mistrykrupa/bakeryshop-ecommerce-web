# Generated by Django 5.0.1 on 2024-02-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0064_alter_item_unique_id_alter_order_payment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='unique_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(default=1, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
