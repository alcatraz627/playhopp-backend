# Generated by Django 2.2.4 on 2019-09-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20190827_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='hopplist',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]
