# Generated by Django 5.1.6 on 2025-03-19 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Blogpost',
        ),
    ]
