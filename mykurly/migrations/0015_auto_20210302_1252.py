# Generated by Django 3.1.4 on 2021-03-02 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mykurly', '0014_order_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Order_item',
        ),
    ]
