# Generated by Django 4.0.6 on 2022-07-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='department',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
