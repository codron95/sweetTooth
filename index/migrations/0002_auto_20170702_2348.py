# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-02 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='foodType',
            field=models.CharField(choices=[('IC', 'Ice Cream'), ('CK', 'Cakes'), ('SW', 'Sweets')], default='IC', max_length=20),
        ),
    ]
