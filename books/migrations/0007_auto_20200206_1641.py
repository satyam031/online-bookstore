# Generated by Django 2.2.9 on 2020-02-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
