# Generated by Django 4.1.5 on 2023-01-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeropress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='brew_time_s',
            field=models.IntegerField(),
        ),
    ]
