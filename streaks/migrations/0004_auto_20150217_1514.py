# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaks', '0003_streak_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='notes',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
