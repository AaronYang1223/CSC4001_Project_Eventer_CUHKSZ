# Generated by Django 4.0.3 on 2022-03-26 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('activity', '0002_alter_activity_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Private_calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_date', models.DateField(auto_now=True)),
                ('is_detele', models.BooleanField(default=False)),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
