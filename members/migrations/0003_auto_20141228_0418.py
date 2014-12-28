# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_streak'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Member'},
        ),
        migrations.AlterModelOptions(
            name='streak',
            options={'verbose_name': 'Member Streak'},
        ),
    ]
