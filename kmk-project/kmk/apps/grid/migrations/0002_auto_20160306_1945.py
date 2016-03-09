# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gridpluginmodel',
            old_name='link',
            new_name='url',
        ),
    ]
