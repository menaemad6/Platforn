# Generated by Django 4.1.7 on 2023-03-12 00:43

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_assignmentsubmit_answer1_assignmentsubmit_answer10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('question_id', models.CharField(max_length=500)),
                ('assignment_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('answer', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Assignment Answer',
                'verbose_name_plural': 'Assignment Answers',
            },
        ),
    ]