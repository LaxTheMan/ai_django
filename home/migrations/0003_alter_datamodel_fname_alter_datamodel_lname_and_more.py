# Generated by Django 4.0.4 on 2022-10-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_datamodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodel',
            name='fname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='lname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]