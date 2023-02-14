# Generated by Django 4.1.6 on 2023-02-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_remove_homecarusel_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeepisode',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='HomeEpisode link'),
        ),
        migrations.AddField(
            model_name='homegenre',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='HomeGenre link'),
        ),
    ]