# Generated by Django 2.0.4 on 2018-04-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20180422_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='value',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Value'),
        ),
    ]