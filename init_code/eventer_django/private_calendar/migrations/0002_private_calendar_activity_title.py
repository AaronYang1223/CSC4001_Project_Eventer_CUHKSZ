# Generated by Django 4.0.3 on 2022-03-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='private_calendar',
            name='activity_title',
            field=models.CharField(default='None', max_length=256),
        ),
    ]