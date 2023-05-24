# Generated by Django 4.1.7 on 2023-04-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_assignmentopen_questions_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
