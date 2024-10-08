# Generated by Django 4.2.10 on 2024-09-21 11:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glassbricks', '0014_alter_property_floor_plan_alter_property_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='floor_plan',
            field=models.TextField(blank=True, max_length=3000, null=True, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='property',
            name='images',
            field=models.TextField(blank=True, max_length=3000, null=True, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='property',
            name='videos',
            field=models.TextField(blank=True, max_length=3000, null=True, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov'])]),
        ),
    ]
