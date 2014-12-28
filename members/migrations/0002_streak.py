# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Streak',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('activity', models.CharField(max_length=50)),
                ('start', models.DateTimeField()),
                ('current_streak', models.IntegerField(default=0)),
                ('longest_streak', models.IntegerField(default=0)),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
                'db_table': 'rel_streaks',
                'verbose_name': 'Member Streaks',
            },
            bases=(models.Model,),
        ),
    ]
