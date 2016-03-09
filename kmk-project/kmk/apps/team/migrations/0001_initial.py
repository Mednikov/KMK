# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(help_text='Please enter a full name for this staff member', max_length=64, default='', verbose_name='full name')),
                ('seniority', models.CharField(help_text='Please enter a full name for this staff member', max_length=64, default='', verbose_name='full name')),
                ('bio', models.TextField(help_text='Please enter a bio for this staff member', max_length=300, default='', blank=True, verbose_name='staff_bio')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
