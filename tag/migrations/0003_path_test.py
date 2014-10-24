# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_path_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='path',
            name='test',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
