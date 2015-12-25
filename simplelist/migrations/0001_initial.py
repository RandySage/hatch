# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sort', models.IntegerField(default=0)),
                ('concept', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('list_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='list',
            field=models.ForeignKey(to='simplelist.List'),
        ),
    ]
