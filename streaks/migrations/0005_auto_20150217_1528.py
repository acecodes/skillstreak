# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaks', '0004_auto_20150217_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='streak',
            name='last_reset',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streak',
            name='resets',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
