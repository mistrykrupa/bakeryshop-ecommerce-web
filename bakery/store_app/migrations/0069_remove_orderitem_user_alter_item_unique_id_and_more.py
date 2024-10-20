# Generated by Django 5.0.1 on 2024-02-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0068_alter_item_unique_id_alter_order_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
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
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
