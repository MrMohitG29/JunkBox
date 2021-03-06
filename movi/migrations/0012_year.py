# Generated by Django 3.0.5 on 2020-06-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movi', '0011_auto_20200608_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default=' ', max_length=20)),
                ('No_of_Movies', models.IntegerField(default=0)),
                ('Movie', models.ManyToManyField(blank=True, related_name='movie', to='movi.Movie')),
            ],
        ),
    ]
