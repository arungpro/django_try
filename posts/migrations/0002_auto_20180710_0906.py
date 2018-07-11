# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name_plural': 'Articles'},
        ),
        migrations.AddField(
            model_name='articles',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 7, 10, 9, 6, 53, 516417), auto_now=True),
            preserve_default=False,
        ),
    ]
