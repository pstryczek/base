# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default='draft', max_length=10, choices=[('draft', 'Roboczy'), ('published', 'Opublikowany')]),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='base.Post', related_name='comments'),
        ),
    ]
