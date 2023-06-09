# Generated by Django 4.1.7 on 2023-04-05 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='is_user',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='last_name',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
