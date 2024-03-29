# Generated by Django 3.1.4 on 2021-02-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mykurly', '0009_delivery_basic_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='calling',
            field=models.CharField(default=1, max_length=12, verbose_name='연락처'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery',
            name='name',
            field=models.CharField(default=2, max_length=20, verbose_name='받을 사람'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delivery',
            name='basic_address',
            field=models.BooleanField(default=False, verbose_name='기본 배송지 설정'),
        ),
    ]
