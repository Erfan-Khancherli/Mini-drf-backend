# Generated by Django 4.2.4 on 2024-03-04 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_remove_profiles_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='profile_image_url',
            new_name='image',
        ),
    ]
