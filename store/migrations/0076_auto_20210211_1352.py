# Generated by Django 3.1.2 on 2021-02-11 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0075_auto_20210209_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 13, 52, 58, 151337)),
        ),
    ]