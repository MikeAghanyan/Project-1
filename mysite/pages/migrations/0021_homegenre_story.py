# Generated by Django 4.1.6 on 2023-02-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_remove_homegenre_story_homeepisode_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='homegenre',
            name='story',
            field=models.TextField(default=1, verbose_name='HomeGenre story'),
            preserve_default=False,
        ),
    ]