# Generated by Django 4.1.7 on 2023-03-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_notification_activity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='liker',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
