# Generated by Django 4.0.1 on 2022-01-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.IntegerField(),
        ),
    ]