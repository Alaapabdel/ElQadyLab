# Generated by Django 4.0.6 on 2022-07-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0008_remove_service_servicesubtitle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discountTitle', models.TextField(max_length=100)),
            ],
        ),
    ]
