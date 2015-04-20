# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaks', '0006_auto_20150225_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='streak',
            options={'verbose_name': 'Member Streak', 'ordering': ['start']},
        ),
    ]
