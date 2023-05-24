# Generated by Django 4.1.7 on 2023-03-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='activity_type',
            field=models.CharField(blank=True, choices=[('charge', 'Charge'), ('purchase', 'Purchase'), ('withdraw', 'Withdraw')], max_length=25),
        ),
    ]
