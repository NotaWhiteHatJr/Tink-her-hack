# Generated by Django 5.0.2 on 2024-03-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_total_price_alter_order_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]