# Generated by Django 2.2.6 on 2019-11-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191101_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_jiomart',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_dmart',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_bigbasket',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
