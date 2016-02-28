# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_teampluginmodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampluginmodel',
            name='seniority',
            field=models.CharField(help_text='Please specify a seniority level for this staff member', blank=True, default='', max_length=64, verbose_name='seniority'),
        ),
    ]
