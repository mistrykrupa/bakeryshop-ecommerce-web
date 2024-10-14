# Generated by Django 5.0.1 on 2024-02-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0066_alter_order_amount_alter_order_paid'),
    ]

    operations = [
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
    ]
