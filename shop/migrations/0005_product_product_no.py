# Generated by Django 3.1 on 2020-10-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201004_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_no',
            field=models.IntegerField(default=0),
        ),
    ]