# Generated by Django 3.2 on 2022-04-16 07:41

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=20, null=True),
        ),
    ]
