# Generated by Django 3.0.2 on 2020-03-22 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0004_auto_20200322_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='enrollment_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='no_dues',
        ),
    ]