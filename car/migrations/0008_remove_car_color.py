# Generated by Django 3.2.4 on 2021-06-11 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_car_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
    ]