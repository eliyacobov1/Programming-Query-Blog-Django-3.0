# Generated by Django 3.0.8 on 2020-08-31 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200831_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='body_part1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image_1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='primary_title',
        ),
    ]