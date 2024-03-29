# Generated by Django 3.1.4 on 2021-02-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mykurly', '0004_auto_20210217_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='번호'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='작성 일자'),
        ),
    ]
