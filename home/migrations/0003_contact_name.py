# Generated by Django 3.2 on 2022-04-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220416_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
