# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmember',
            name='bio',
            field=models.TextField(default='', blank=True, max_length=300, help_text='Please enter a bio for this staff member', verbose_name='staff_bio'),
        ),
    ]
