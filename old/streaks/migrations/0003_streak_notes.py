# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaks', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='streak',
            name='notes',
            field=models.CharField(null=True, max_length=300),
            preserve_default=True,
        ),
    ]
