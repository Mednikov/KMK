# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20160224_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappoint',
            name='name',
            field=models.CharField(max_length=140, verbose_name='address', help_text='Please enter an organisation name', default=''),
        ),
    ]
