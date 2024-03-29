# Generated by Django 5.0.2 on 2024-03-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_poster_product_p_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_qty',
            field=models.IntegerField(default=0),
        ),
    ]
