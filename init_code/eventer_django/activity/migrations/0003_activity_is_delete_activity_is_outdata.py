# Generated by Django 4.0.3 on 2022-03-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_alter_activity_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='is_outdata',
            field=models.BooleanField(default=False),
        ),
    ]
