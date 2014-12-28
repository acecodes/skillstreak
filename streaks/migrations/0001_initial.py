# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20141227_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Streak',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.CharField(max_length=50)),
                ('start', models.DateTimeField()),
                ('current_streak', models.IntegerField(default=0)),
                ('longest_streak', models.IntegerField(default=0)),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
                'verbose_name': 'Member Streak',
                'db_table': 'rel_streaks',
            },
            bases=(models.Model,),
        ),
    ]
