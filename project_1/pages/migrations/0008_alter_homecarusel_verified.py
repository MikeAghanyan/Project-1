# Generated by Django 4.1.6 on 2023-02-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_homecarusel_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecarusel',
            name='verified',
            field=models.ImageField(upload_to='media', verbose_name='HomeCarusel verified image'),
        ),
    ]
