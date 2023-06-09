# Generated by Django 4.1.7 on 2023-03-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_assignment_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmit',
            name='false_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='true_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='post_id',
            field=models.CharField(blank=True, default='none', max_length=500),
        ),
    ]
