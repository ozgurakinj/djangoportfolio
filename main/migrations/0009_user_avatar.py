# Generated by Django 3.2.3 on 2021-10-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211014_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=1, upload_to='avatar'),
            preserve_default=False,
        ),
    ]
