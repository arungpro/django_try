# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'The Book', max_length=225)),
                ('author', models.CharField(default=b'anonymous', max_length=225)),
                ('details', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'pizza',
            },
            bases=(models.Model,),
        ),
    ]
