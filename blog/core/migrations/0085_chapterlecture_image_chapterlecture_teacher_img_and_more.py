# Generated by Django 4.1.7 on 2023-05-17 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_chapterlecture_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapterlecture',
            name='image',
            field=models.ImageField(default='none.jpeg', upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='chapterlecture',
            name='teacher_img',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_images'),
        ),
        migrations.AddField(
            model_name='chapterlecture',
            name='teacher_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='chapterlecture',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]