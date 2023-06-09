# Generated by Django 4.2 on 2023-04-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('is_sale', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
                ('photo', models.ImageField(upload_to='Product')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
