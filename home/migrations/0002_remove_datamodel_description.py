# Generated by Django 4.0.4 on 2022-10-29 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datamodel',
            name='description',
        ),
    ]