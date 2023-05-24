# Generated by Django 4.1.7 on 2023-05-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0103_buychapter_image_buychapter_method_buychapter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buychapter',
            name='method',
            field=models.CharField(blank=True, choices=[('wallet', 'Wallet'), ('code', 'Code'), ('chapter_code', 'Chapter Code')], default='code', max_length=25),
        ),
    ]
