# Generated by Django 4.1.7 on 2023-05-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0087_rename_chapter_id_chapter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='year',
            field=models.CharField(blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], default='first', max_length=25),
        ),
    ]
