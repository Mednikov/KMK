# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='cms.CMSPlugin', serialize=False, primary_key=True)),
                ('heading', models.CharField(help_text='Please enter a heading for this post', verbose_name='heading', default='', max_length=120)),
                ('heading_link', models.CharField(help_text='Please enter a heading link for this post', verbose_name='heading link', default='', blank=True, max_length=200)),
                ('description', models.TextField(help_text='Please enter a description for this post', verbose_name='description', default='', blank=True, max_length=300)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', help_text='Please supply an image of this post', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
