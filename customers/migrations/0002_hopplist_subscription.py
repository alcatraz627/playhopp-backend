# Generated by Django 2.2.4 on 2019-08-27 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0003_toy_primaryimage'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoppList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('toys', models.ManyToManyField(to='toys.Toy')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='')),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('hopplist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.HoppList')),
            ],
        ),
    ]