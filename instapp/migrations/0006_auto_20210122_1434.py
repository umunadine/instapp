# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-22 12:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instapp', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['caption']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user']},
        ),
        migrations.AddField(
            model_name='follow',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instapp.Profile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
