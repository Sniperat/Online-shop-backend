# Generated by Django 4.0 on 2022-03-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_product_subcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
