# Generated by Django 4.2.6 on 2023-10-31 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quora_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='Comment',
        ),
        migrations.AlterModelTable(
            name='post',
            table='Post',
        ),
    ]
