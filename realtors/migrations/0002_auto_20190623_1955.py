# Generated by Django 2.2.2 on 2019-06-24 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Realtors',
            new_name='Realtor',
        ),
    ]