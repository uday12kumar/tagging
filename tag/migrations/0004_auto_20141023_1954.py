# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_path_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='path',
            name='name',
        ),
        migrations.RemoveField(
            model_name='path',
            name='test',
        ),
    ]
