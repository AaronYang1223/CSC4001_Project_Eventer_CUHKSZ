# Generated by Django 4.0.3 on 2022-04-08 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0013_activity_is_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='content',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='activity',
            name='tag',
            field=models.CharField(max_length=1024),
        ),
    ]
