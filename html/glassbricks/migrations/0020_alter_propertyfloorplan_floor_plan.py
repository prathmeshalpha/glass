# Generated by Django 4.2.10 on 2024-09-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glassbricks', '0019_alter_propertyfloorplan_floor_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyfloorplan',
            name='floor_plan',
            field=models.FileField(upload_to='property_floor_plan/'),
        ),
    ]
