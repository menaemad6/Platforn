# Generated by Django 4.1.7 on 2023-04-06 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_remove_part_id_part_part_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='type',
            field=models.CharField(blank=True, choices=[('video', 'Video'), ('video2', 'Video2'), ('video3', 'Video3'), ('video4', 'Video4'), ('video5', 'Video5')], max_length=25),
        ),
    ]
