# Generated by Django 2.2.4 on 2019-09-23 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20190923_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='hopplist',
        ),
        migrations.AddField(
            model_name='subscription',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
