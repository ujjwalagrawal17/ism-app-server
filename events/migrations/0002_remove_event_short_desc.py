# Generated by Django 2.1.7 on 2019-03-18 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='short_desc',
        ),
    ]
