# Generated by Django 4.1.7 on 2023-04-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_answer_question_true_alter_answer_true'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='assignment_name',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
