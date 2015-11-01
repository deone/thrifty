# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
