# Generated by Django 4.0.3 on 2022-04-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_tag',
            field=models.CharField(max_length=1024),
        ),
    ]
