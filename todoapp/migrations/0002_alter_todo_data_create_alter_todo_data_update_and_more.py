# Generated by Django 4.0.3 on 2022-08-30 09:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='data_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 30, 9, 41, 2, 900255, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='data_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 1, 9, 41, 2, 900255, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default='-', on_delete=django.db.models.deletion.CASCADE, to='todoapp.project'),
        ),
    ]
