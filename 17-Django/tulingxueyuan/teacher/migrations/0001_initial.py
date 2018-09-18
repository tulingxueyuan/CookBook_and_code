# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=12)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]
