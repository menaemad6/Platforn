# Generated by Django 4.1.7 on 2023-03-01 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_attach1_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='attach1_name',
        ),
    ]
