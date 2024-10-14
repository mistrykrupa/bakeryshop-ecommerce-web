# Generated by Django 5.0.1 on 2024-02-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0058_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
