# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('lat', models.CharField(default='', help_text='Please enter a latitude', verbose_name='latitude', max_length=16)),
                ('lon', models.CharField(default='', help_text='Please enter a longitude', verbose_name='longitude', max_length=16)),
            ],
        ),
    ]
