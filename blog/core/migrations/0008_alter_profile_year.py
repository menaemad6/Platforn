# Generated by Django 4.1.7 on 2023-03-03 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_post_attach3_link_post_attach3_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('none', 'None')], default='none', max_length=25, null=True),
        ),
    ]