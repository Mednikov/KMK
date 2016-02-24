# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_mappoint_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mappoint',
            name='adress',
        ),
        migrations.AddField(
            model_name='mappoint',
            name='address',
            field=models.CharField(default='', help_text='Please enter a contact adress', verbose_name='address', max_length=140),
        ),
    ]
