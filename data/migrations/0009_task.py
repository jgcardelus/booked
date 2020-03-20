# Generated by Django 3.0.4 on 2020-03-20 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_meeting_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=512)),
                ('due_date', models.DateTimeField()),
                ('notes', models.CharField(max_length=2048)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Group')),
            ],
        ),
    ]
