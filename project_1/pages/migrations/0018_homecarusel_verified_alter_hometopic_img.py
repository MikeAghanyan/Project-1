# Generated by Django 4.1.6 on 2023-02-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_remove_homecarusel_img2'),
    ]

    operations = [
        migrations.AddField(
            model_name='homecarusel',
            name='verified',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='HomeCarusel verified image'),
        ),
        migrations.AlterField(
            model_name='hometopic',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='HomeTopic image'),
        ),
    ]