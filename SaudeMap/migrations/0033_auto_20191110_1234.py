# Generated by Django 2.2.6 on 2019-11-10 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SaudeMap', '0032_auto_20191110_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fichadoenca',
            old_name='longetude',
            new_name='longitude',
        ),
    ]