# Generated by Django 4.2.6 on 2023-11-30 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0008_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default_image/Defaut.png', upload_to='profile_pics'),
        ),
    ]
