# Generated by Django 3.1.2 on 2020-12-31 05:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_chefreview_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefreview',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='chefreview',
            name='rating',
            field=models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
