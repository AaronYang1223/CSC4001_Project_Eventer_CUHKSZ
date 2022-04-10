# Generated by Django 4.0.3 on 2022-03-27 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_picture'),
        ('activity', '0008_activity_part_max_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='originizer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='originizer_id', to='user.user'),
        ),
    ]