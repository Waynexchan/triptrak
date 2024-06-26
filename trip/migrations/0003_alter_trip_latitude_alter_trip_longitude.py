# Generated by Django 5.0.4 on 2024-04-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_trip_latitude_trip_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True),
        ),
    ]
