# Generated by Django 3.2.7 on 2021-09-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_auto_20210929_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='joined',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lives',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
