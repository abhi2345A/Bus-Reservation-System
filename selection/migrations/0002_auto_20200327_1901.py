# Generated by Django 3.0.2 on 2020-03-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_type',
            new_name='seat_type',
        ),
    ]