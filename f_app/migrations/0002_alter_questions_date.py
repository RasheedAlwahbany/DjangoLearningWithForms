# Generated by Django 3.2.10 on 2022-01-04 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
