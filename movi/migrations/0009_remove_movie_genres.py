# Generated by Django 3.0.5 on 2020-06-07 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movi', '0008_auto_20200607_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
    ]