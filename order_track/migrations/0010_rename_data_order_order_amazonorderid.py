# Generated by Django 4.1.1 on 2023-01-24 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order_track", "0009_alter_order_data_order"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order", old_name="Data_Order", new_name="AmazonOrderId",
        ),
    ]