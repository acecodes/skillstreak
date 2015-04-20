# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaks', '0009_auto_20150227_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='last_reset',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='streak',
            name='start',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
