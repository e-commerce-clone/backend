# Generated by Django 3.1.4 on 2021-02-17 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210207_1538'),
        ('accounts', '0001_initial'),
        ('mykurly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='writer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='helps',
            field=models.PositiveIntegerField(default=0, verbose_name='도움이 돼요'),
        ),
        migrations.AlterField(
            model_name='review',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]
