# Generated by Django 3.2.7 on 2021-09-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_delete_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_pic_path',
            field=models.CharField(default='\\media\\default_cover.png', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic_path',
            field=models.CharField(default='\\media\\default_profile.png', max_length=200),
        ),
    ]
