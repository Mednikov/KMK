# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20160224_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('lat', models.CharField(verbose_name='latitude', max_length=16, help_text='Please enter a latitude', default='')),
                ('lon', models.CharField(verbose_name='longitude', max_length=16, help_text='Please enter a longitude', default='')),
            ],
        ),
    ]
