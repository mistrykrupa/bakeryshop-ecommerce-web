# Generated by Django 5.0.1 on 2024-02-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0070_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(default='1', max_length=100, null=True),
        ),
    ]
