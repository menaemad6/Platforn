# Generated by Django 4.1.7 on 2023-03-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_code_code_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
