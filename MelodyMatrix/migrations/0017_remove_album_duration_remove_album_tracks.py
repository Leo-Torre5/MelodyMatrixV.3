# Generated by Django 4.2.6 on 2023-11-30 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MelodyMatrix', '0016_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='album',
            name='tracks',
        ),
    ]
