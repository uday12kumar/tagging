# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='path',
            name='name',
            field=models.CharField(default=datetime.datetime(2014, 10, 23, 19, 52, 47, 605826, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
