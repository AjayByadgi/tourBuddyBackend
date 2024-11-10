# Generated by Django 4.2.6 on 2024-11-10 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_remove_landmark_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='landmark',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='landmark',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]