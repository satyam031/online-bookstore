# Generated by Django 2.2.9 on 2020-02-14 07:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20200213_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
