# Generated by Django 4.1.1 on 2023-01-24 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order_track", "0005_orderfiledata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="Order",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]