# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20160224_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffmember',
            old_name='name',
            new_name='full_name',
        ),
    ]
