# Generated by Django 4.2.6 on 2023-11-10 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MelodyMatrix', '0007_remove_artist_album_image_album_album_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'permissions': (('can_add_album_instance', 'Can add album instances'),)},
        ),
    ]
