# Generated by Django 4.2.4 on 2024-03-04 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='name',
        ),
    ]
