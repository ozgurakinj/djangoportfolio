# Generated by Django 3.2.3 on 2021-08-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_year',
            field=models.IntegerField(),
        ),
    ]