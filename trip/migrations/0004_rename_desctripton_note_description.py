# Generated by Django 5.0.4 on 2024-04-09 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_alter_trip_latitude_alter_trip_longitude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='desctripton',
            new_name='description',
        ),
    ]
