# Generated by Django 4.0.6 on 2022-07-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0005_alter_service_servicebody_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionTitle', models.CharField(max_length=100)),
                ('optionTitleAR', models.CharField(max_length=100)),
                ('optionBody', models.TextField(max_length=500)),
                ('optionBodyAR', models.TextField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='serviceImage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='serviceBody',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='service',
            name='serviceBodyAR',
            field=models.TextField(max_length=2000),
        ),
    ]
