# Generated by Django 3.1 on 2021-04-06 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0005_auto_20210406_0806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-date']},
        ),
    ]
