# Generated by Django 3.0.2 on 2020-03-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0004_auto_20200327_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]