# Generated by Django 3.2 on 2022-04-15 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_userprofile_default_county'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_country',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
