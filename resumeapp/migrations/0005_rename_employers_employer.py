# Generated by Django 3.2.7 on 2021-09-09 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_employers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employers',
            new_name='Employer',
        ),
    ]
