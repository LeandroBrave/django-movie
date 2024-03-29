# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('genre', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
                ('price', models.DecimalField(max_digits=20, decimal_places=0)),
            ],
        ),
    ]
