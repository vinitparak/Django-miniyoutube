# Generated by Django 2.2.4 on 2019-09-27 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vibg',
            name='date_added',
        ),
    ]
