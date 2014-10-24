# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0004_auto_20141023_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeCrossing', models.CharField(max_length=100)),
                ('busStop', models.CharField(max_length=100)),
                ('barrier', models.CharField(max_length=100)),
                ('sidewalk', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('improvement', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='path',
            old_name='access',
            new_name='slope',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='buildingRequest',
            new_name='smoothness',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='elevator',
            new_name='surface',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='toilets',
            new_name='way',
        ),
        migrations.AddField(
            model_name='path',
            name='width',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
