# Generated by Django 4.0.3 on 2022-04-02 13:48

import activity.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0011_activity_score_avg_activity_score_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='cover_page',
            field=imagekit.models.fields.ProcessedImageField(default='activicity/default.png', upload_to=activity.models.cover_dictory),
        ),
    ]
