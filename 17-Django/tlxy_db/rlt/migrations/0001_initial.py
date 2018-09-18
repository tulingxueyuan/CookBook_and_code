# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('manager_id', models.IntegerField()),
                ('manager_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('school_id', models.IntegerField()),
                ('school_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='my_school',
            field=models.OneToOneField(to='rlt.School'),
        ),
    ]
