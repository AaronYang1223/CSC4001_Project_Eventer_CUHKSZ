# Generated by Django 4.0.3 on 2022-04-08 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_comment', '0003_activity_comment_activity_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_comment',
            name='content',
            field=models.CharField(max_length=1024),
        ),
    ]
