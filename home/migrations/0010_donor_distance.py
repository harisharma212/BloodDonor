# Generated by Django 4.2 on 2023-04-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210810_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='distance',
            field=models.FloatField(default=0.0),
        ),
    ]
