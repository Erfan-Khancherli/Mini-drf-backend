# Generated by Django 4.2.4 on 2024-01-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camera_Files', '0002_gtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtoken',
            name='gtoken',
            field=models.CharField(default='0'),
        ),
    ]
