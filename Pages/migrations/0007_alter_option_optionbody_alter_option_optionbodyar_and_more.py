# Generated by Django 4.0.6 on 2022-07-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0006_option_service_serviceimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='optionBody',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='option',
            name='optionBodyAR',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='service',
            name='serviceBody',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='service',
            name='serviceBodyAR',
            field=models.TextField(max_length=3000),
        ),
    ]
