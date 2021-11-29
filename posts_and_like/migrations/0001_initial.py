# Generated by Django 3.1.3 on 2021-10-03 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '0015_auto_20211003_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postinfo', models.TextField(max_length=400)),
                ('likecount', models.IntegerField(default=0)),
                ('timeday', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_auth.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isliked', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_and_like.post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_auth.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=500)),
                ('comment_relation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts_and_like.post')),
            ],
        ),
    ]
