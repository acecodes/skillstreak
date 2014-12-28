# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20141228_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streak',
            name='member',
        ),
        migrations.DeleteModel(
            name='Streak',
        ),
    ]
