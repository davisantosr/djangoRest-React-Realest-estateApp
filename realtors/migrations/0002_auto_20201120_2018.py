# Generated by Django 3.1.3 on 2020-11-20 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='date_hired',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 20, 20, 18, 2, 421651)),
        ),
    ]
