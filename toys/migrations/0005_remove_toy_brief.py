# Generated by Django 2.2.4 on 2019-09-03 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0004_auto_20190827_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toy',
            name='brief',
        ),
    ]
