# Generated by Django 3.0.4 on 2020-03-21 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_joinedgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_teacher',
            new_name='is_admin',
        ),
    ]
