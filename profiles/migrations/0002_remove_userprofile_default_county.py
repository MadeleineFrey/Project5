# Generated by Django 3.2 on 2022-04-15 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_county',
        ),
    ]
