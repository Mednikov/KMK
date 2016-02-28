# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20160228_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampluginmodel',
            name='seniority',
            field=models.ForeignKey(help_text='Please specify a seniority level for this staff member', null=True, blank=True, default=None, to='staff.Seniority'),
        ),
    ]
