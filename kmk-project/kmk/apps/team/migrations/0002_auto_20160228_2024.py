# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampluginmodel',
            name='seniority',
            field=models.CharField(help_text='Please enter a full name for this staff member', default='', verbose_name='seniority', max_length=64),
        ),
    ]
