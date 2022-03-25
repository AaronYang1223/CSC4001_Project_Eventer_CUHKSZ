# Generated by Django 4.0.3 on 2022-03-25 14:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_tag', models.CharField(max_length=32)),
                ('post_title', models.CharField(max_length=256)),
                ('post_content', ckeditor.fields.RichTextField()),
                ('comment_number', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='user.user')),
            ],
        ),
    ]
