# Generated by Django 2.2.17 on 2021-01-26 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210126_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='note',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 26, 2, 9, 26, 628547)),
        ),
    ]
