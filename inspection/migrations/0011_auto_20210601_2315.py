# Generated by Django 3.1 on 2021-06-01 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0010_auto_20210601_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='taking_benefit',
            new_name='currently_receiving',
        ),
    ]