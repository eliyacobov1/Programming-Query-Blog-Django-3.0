# Generated by Django 3.0.8 on 2020-09-06 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200906_1531'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
