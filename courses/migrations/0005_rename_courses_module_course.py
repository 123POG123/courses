# Generated by Django 3.2.9 on 2021-11-23 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20211123_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='courses',
            new_name='course',
        ),
    ]
