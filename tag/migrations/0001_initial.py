# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buildingRequest', models.CharField(max_length=100)),
                ('wheelchair', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('improvement', models.CharField(max_length=100)),
                ('elevator', models.CharField(max_length=100)),
                ('toilets', models.CharField(max_length=100)),
                ('access', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buildingRequest', models.CharField(max_length=100)),
                ('wheelchair', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('improvement', models.CharField(max_length=100)),
                ('elevator', models.CharField(max_length=100)),
                ('toilets', models.CharField(max_length=100)),
                ('access', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
