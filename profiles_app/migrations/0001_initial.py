# Generated by Django 4.0.1 on 2022-02-07 13:14

import django.core.validators
from django.db import migrations, models
import profiles_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('username', models.CharField(blank=True, max_length=40, null=True, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='surname')),
                ('phone', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999 Up to 15 digits allowed.', regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='registered')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is_superuser')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='avatar')),
                ('city', models.CharField(blank=True, max_length=40, null=True, verbose_name='city')),
                ('address', models.CharField(blank=True, max_length=70, null=True, verbose_name='address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', profiles_app.models.UserManager()),
            ],
        ),
    ]
