# Generated by Django 4.2.3 on 2023-07-22 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userimage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='Image',
        ),
    ]
