# Generated by Django 4.2.6 on 2023-11-21 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0006_remove_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
