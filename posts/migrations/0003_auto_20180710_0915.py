# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180710_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
