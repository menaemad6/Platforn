# Generated by Django 4.1.7 on 2023-03-11 16:25

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_assigment_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignment_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('student', models.CharField(blank=True, max_length=100)),
                ('assigment_name', models.CharField(blank=True, max_length=100)),
                ('no_of_applicants', models.IntegerField(blank=True, default='0')),
                ('assigment_type', models.CharField(blank=True, choices=[('test', 'Test'), ('homework', 'Homework')], max_length=25)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Assignment',
                'verbose_name_plural': 'Assignments',
            },
        ),
        migrations.DeleteModel(
            name='Assigment',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='assigment_id',
            new_name='assignment_id',
        ),
    ]
