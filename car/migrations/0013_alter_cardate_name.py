# Generated by Django 3.2.4 on 2021-06-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0012_alter_cardate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardate',
            name='name',
            field=models.CharField(max_length=4),
        ),
    ]
