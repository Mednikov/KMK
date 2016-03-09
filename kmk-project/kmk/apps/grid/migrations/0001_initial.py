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
            name='GridPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', auto_created=True, primary_key=True, parent_link=True, serialize=False)),
                ('alt', models.CharField(blank=True, max_length=120, help_text='Optional. Please enter an alternative text for image', verbose_name='alt', default='')),
                ('link', models.CharField(blank=True, max_length=200, help_text='Optional. Please enter an URL for this image (example: http://ya.ru)', verbose_name='URL', default='')),
                ('img', filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.Image', help_text='Please supply an image.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
