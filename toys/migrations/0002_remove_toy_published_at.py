# Generated by Django 2.2.4 on 2019-08-27 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toy',
            name='published_at',
        ),
    ]