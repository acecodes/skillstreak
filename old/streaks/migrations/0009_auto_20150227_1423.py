# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaks', '0008_auto_20150226_1050'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='streak',
            unique_together=set([('user', 'activity')]),
        ),
    ]
