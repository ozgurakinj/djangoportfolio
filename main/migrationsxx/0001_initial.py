# Generated by Django 3.2.3 on 2021-12-23 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import main.models
import portfolio.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('avatar', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=75, size=[400, 400], storage=portfolio.storage.OverwriteStorage(), upload_to=main.models.photo_path)),
                ('name', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('biography', models.TextField(max_length=220)),
                ('location', models.CharField(max_length=50)),
                ('color', models.CharField(choices=[('primary', 'Blue'), ('danger', 'Red'), ('success', 'Green'), ('warning', 'Yellow'), ('info', 'Cyan'), ('secondary', 'Grey')], default='primary', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField(choices=[(1, 'Beginner'), (2, 'Elementary'), (3, 'Intermediate'), (4, 'Advanced'), (5, 'Expert')], default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField(choices=[(1, 'Beginner'), (2, 'Elementary'), (3, 'Intermediate'), (4, 'Advanced'), (5, 'Native')], default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('position', models.CharField(max_length=50)),
                ('firm', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('department', models.CharField(blank=True, max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('is_highschool', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('certificate', 'Certificate'), ('award', 'Award')], default='certificate', max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('year', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]
