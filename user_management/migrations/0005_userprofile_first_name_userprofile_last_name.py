# Generated by Django 4.2.6 on 2023-11-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_userprofile_address_userprofile_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
