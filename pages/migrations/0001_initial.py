# Generated by Django 4.0.1 on 2022-01-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('age', models.TextField(default='00', max_length=50)),
                ('phone', models.IntegerField(max_length=11)),
            ],
        ),
    ]
