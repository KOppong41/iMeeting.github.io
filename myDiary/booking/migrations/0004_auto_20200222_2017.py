# Generated by Django 3.0.2 on 2020-02-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20200222_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingplace',
            name='place_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
