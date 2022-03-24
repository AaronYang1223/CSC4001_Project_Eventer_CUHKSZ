# Generated by Django 4.0.3 on 2022-03-24 10:15

import activity.models
import ckeditor.fields
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=32)),
                ('start_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('content', ckeditor.fields.RichTextField()),
                ('comment_number', models.IntegerField(default=0)),
                ('cover_page', imagekit.models.fields.ProcessedImageField(default='media/activicity/default.png', upload_to=activity.models.cover_dictory)),
            ],
        ),
    ]
