# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20160228_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampluginmodel',
            name='email',
            field=models.CharField(help_text='Please enter an e-mail for this staff member', blank=True, max_length=64, verbose_name='e-mail', default=''),
        ),
        migrations.AddField(
            model_name='teampluginmodel',
            name='phone',
            field=models.CharField(help_text='Please enter a phone number for this staff member', blank=True, max_length=64, verbose_name='phone', default=''),
        ),
    ]
