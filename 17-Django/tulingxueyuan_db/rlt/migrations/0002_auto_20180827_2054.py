# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rlt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='my_school',
            field=models.OneToOneField(to='rlt.School'),
        ),
    ]
