# Generated by Django 3.2.4 on 2021-06-11 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_auto_20210611_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.carcolor'),
        ),
    ]
