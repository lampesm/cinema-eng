# Generated by Django 4.0.4 on 2022-04-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_remove_chair_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='firstname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='myuser',
            name='lastname',
            field=models.CharField(default=None, max_length=50),
        ),
    ]