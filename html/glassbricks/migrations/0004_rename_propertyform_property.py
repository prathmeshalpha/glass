# Generated by Django 4.2.10 on 2024-08-28 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glassbricks', '0003_propertyform_propertyimage_delete_property'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PropertyForm',
            new_name='Property',
        ),
    ]
