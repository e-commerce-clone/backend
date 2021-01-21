# Generated by Django 3.1.4 on 2021-01-20 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210116_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='main_image',
            field=models.ImageField(upload_to='products/mainImage/%Y/%m/%d', verbose_name='메인 이미지'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='sub_image',
            field=models.ImageField(upload_to='products/subImage/%Y/%m/%d', verbose_name='서브 이미지'),
        ),
    ]
