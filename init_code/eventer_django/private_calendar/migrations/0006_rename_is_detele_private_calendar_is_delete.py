# Generated by Django 4.0.3 on 2022-04-10 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_calendar', '0005_alter_private_calendar_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='private_calendar',
            old_name='is_detele',
            new_name='is_delete',
        ),
    ]
