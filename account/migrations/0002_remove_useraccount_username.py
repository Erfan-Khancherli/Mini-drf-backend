# Generated by Django 4.2.4 on 2023-12-19 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='username',
        ),
    ]