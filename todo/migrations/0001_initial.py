# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoEnvet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=1024, verbose_name=b'\xe5\xbe\x85\xe5\x8a\x9e\xe4\xba\x8b\xe9\xa1\xb9\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
        ),
    ]
