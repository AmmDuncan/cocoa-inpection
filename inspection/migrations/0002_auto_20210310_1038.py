# Generated by Django 3.1 on 2021-03-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='deed_status',
            field=models.CharField(choices=[('', 'select...'), ('c', 'COMPLETED')], max_length=5, verbose_name='Deed of Assignment'),
        ),
    ]
