# Generated by Django 3.0.4 on 2020-03-21 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinedGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.User')),
            ],
        ),
    ]
