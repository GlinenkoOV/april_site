# Generated by Django 4.2 on 2023-04-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_popular_alter_product_is_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popular',
            name='desc',
            field=models.TextField(max_length=200),
        ),
    ]
