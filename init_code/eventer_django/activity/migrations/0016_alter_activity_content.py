# Generated by Django 4.0.3 on 2022-04-17 00:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0015_alter_activity_cover_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
