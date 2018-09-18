# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rlt', '0002_auto_20180827_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('teacher_name', models.CharField(max_length=20)),
                ('schools', models.ForeignKey(to='rlt.School')),
            ],
        ),
    ]
