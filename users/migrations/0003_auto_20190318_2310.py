# Generated by Django 2.1.7 on 2019-03-18 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190304_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='club',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
