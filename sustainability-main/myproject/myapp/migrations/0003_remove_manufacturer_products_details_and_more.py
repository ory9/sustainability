# Generated by Django 5.0.2 on 2024-03-17 15:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_manufacturer_product_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="manufacturer",
            name="products_details",
        ),
        migrations.RemoveField(
            model_name="products",
            name="product_manufacture_date",
        ),
        migrations.RemoveField(
            model_name="products",
            name="product_name",
        ),
        migrations.RemoveField(
            model_name="products",
            name="product_quantity",
        ),
        migrations.RemoveField(
            model_name="products",
            name="product_type",
        ),
        migrations.AddField(
            model_name="manufacturer",
            name="product_expiry_date",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="Expiry Date"
            ),
        ),
        migrations.AddField(
            model_name="manufacturer",
            name="product_mf_date",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Manufacturing Date"
            ),
        ),
        migrations.AddField(
            model_name="manufacturer",
            name="product_name",
            field=models.CharField(
                default="Unknown", max_length=50, verbose_name="Product Name"
            ),
        ),
        migrations.AddField(
            model_name="manufacturer",
            name="product_type",
            field=models.CharField(
                choices=[("RC", "Recycable"), ("NRC", "Non Recycable")],
                default="RC",
                max_length=50,
                verbose_name="Product Type",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="manufacturer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.manufacturer",
                verbose_name="",
            ),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="manufacturer_name",
            field=models.CharField(
                default="Unknown", max_length=50, verbose_name="Company Name"
            ),
        ),
    ]
