# Generated by Django 4.1.7 on 2023-04-19 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_question_assignment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
