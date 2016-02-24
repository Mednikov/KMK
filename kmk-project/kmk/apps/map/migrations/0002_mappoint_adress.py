# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappoint',
            name='adress',
            field=models.CharField(help_text='Please enter a contact adress', max_length=140, verbose_name='adress', default=''),
        ),
    ]
