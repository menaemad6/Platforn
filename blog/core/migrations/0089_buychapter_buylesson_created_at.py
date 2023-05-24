# Generated by Django 4.1.7 on 2023-05-18 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0088_chapter_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Chapter Purchase',
                'verbose_name_plural': 'Chapter Purchases',
            },
        ),
        migrations.AddField(
            model_name='buylesson',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
