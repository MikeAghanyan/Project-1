# Generated by Django 4.1.6 on 2023-02-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_aboutpodcaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometopic',
            name='story',
            field=models.TextField(default=1, verbose_name='HomeTopic story'),
            preserve_default=False,
        ),
    ]