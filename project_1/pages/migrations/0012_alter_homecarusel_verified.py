# Generated by Django 4.1.6 on 2023-02-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_hometopic_alter_homecarusel_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecarusel',
            name='verified',
            field=models.ImageField(blank=True, upload_to='', verbose_name='HomeCarusel verified image'),
        ),
    ]
