# Generated by Django 4.1.7 on 2023-04-10 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_alter_info_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Information', 'verbose_name_plural': 'Information '},
        ),
        migrations.AddField(
            model_name='assignment',
            name='questions_count',
            field=models.IntegerField(default=0),
        ),
    ]
