# Generated by Django 5.0.7 on 2024-07-20 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='drinks',
            new_name='drink',
        ),
    ]
