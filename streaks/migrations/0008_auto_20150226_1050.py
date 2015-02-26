# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaks', '0007_auto_20150226_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='streak',
            options={'ordering': ['-start'], 'verbose_name': 'Member Streak'},
        ),
    ]
