# Generated by Django 4.0.3 on 2022-04-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_comment', '0002_post_comment_post_id_delete_comment_post_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comment',
            name='content',
            field=models.CharField(max_length=1024),
        ),
    ]
