# Generated by Django 4.1.6 on 2023-02-14 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_homecarusel_boolean_homecarusel_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homecarusel',
            name='verified',
        ),
    ]