# Generated by Django 4.0.3 on 2022-04-10 02:01

import activity.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0014_alter_activity_content_alter_activity_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='cover_page',
            field=imagekit.models.fields.ProcessedImageField(default='activity/default.png', upload_to=activity.models.cover_dictory),
        ),
    ]