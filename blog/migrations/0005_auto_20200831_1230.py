# Generated by Django 3.0.8 on 2020-08-31 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200831_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body_part1',
            new_name='body_part_1',
        ),
    ]
