# Generated by Django 4.1.7 on 2023-03-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_code_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentopen',
            name='assignment_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='assignment_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]