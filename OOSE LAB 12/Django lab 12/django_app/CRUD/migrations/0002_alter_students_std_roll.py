# Generated by Django 3.2.11 on 2022-01-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='std_roll',
            field=models.CharField(default='', max_length=50),
        ),
    ]
