# Generated by Django 4.1.7 on 2023-03-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_age_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('professions', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='image')),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'userdetail',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
    ]
