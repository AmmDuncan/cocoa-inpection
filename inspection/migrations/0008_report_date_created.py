# Generated by Django 3.1 on 2021-04-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0007_manager_after_and'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
