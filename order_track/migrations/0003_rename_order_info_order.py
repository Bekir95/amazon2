# Generated by Django 4.1.1 on 2023-01-13 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_data_maliyet"),
        ("order_track", "0002_order_info_order_alter_order_info_tracknumber"),
    ]

    operations = [
        migrations.RenameModel(old_name="Order_Info", new_name="Order",),
    ]
