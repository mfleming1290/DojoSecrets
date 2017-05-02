# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-30 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secrets', to='log.User')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='secret_like',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secret_likes', to='secret.Secret'),
        ),
        migrations.AddField(
            model_name='like',
            name='user_like',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to='log.User'),
        ),
    ]