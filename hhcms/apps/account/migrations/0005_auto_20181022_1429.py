# Generated by Django 2.0.4 on 2018-10-22 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20181022_1428'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Property',
            new_name='UserProperty',
        ),
    ]
