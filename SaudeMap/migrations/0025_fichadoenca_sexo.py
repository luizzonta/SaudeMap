# Generated by Django 2.2.6 on 2019-11-09 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SaudeMap', '0024_auto_20191108_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichadoenca',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=120, null=True),
        ),
    ]
