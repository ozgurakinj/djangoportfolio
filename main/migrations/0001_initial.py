# Generated by Django 3.2.3 on 2021-08-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField(max_length=4)),
                ('end_year', models.IntegerField(max_length=4)),
                ('department', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('is_highschool', models.BooleanField()),
            ],
        ),
    ]
