# Generated by Django 2.0.4 on 2018-05-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20180521_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
