# Generated by Django 3.1.6 on 2021-02-25 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210225_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channelvilla',
            old_name='channel_name',
            new_name='channel_name_main',
        ),
    ]