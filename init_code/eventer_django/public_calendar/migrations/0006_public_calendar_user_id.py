# Generated by Django 4.0.3 on 2022-04-02 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_first_name'),
        ('public_calendar', '0005_alter_public_calendar_activity_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='public_calendar',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
