# Generated by Django 3.1.4 on 2021-03-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_item',
            name='order_type',
            field=models.CharField(default='결제완료', max_length=100, verbose_name='주문상태'),
        ),
    ]
