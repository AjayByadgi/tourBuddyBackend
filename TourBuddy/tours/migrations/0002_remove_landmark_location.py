# Generated by Django 4.2.6 on 2024-11-09 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landmark',
            name='location',
        ),
    ]