# Generated by Django 4.2 on 2023-04-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('desc', models.TextField(blank=True, max_length=200)),
                ('photo', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=True),
        ),
    ]