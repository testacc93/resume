# Generated by Django 3.1.5 on 2021-09-08 16:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0002_auto_20210908_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hobbies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=None),
        ),
    ]
