# Generated by Django 4.1.1 on 2023-01-24 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_data_maliyet"),
        ("order_track", "0006_alter_order_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="Order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.data",
            ),
        ),
    ]
