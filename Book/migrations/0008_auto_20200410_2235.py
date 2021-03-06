# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-04-10 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0007_auto_20200410_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_tag',
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='Book.Tag'),
        ),
        migrations.AlterField(
            model_name='book',
            name='related_books',
            field=models.ManyToManyField(blank=True, null=True, to='Book.Book'),
        ),
    ]
