# Generated by Django 3.1.4 on 2020-12-17 12:09

from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('nickname', models.CharField(blank=True, max_length=50, unique=True, verbose_name='nickname')),
                ('profile_picture', models.ImageField(blank=True, upload_to=user.models.upload_to, verbose_name='profile_picture')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, verbose_name='gender')),
                ('age', models.CharField(blank=True, choices=[('10-', '10-'), ('10-20', '10-20'), ('20-30', '20-30'), ('30-40', '30-40'), ('40-50', '40-50'), ('50-60', '50-60'), ('60+', '60+')], max_length=50, verbose_name='age')),
                ('race', models.CharField(blank=True, choices=[('American Indian / Alaska Native', 'American Indian / Alaska Native'), ('Asian', 'Asian'), ('Black / African American', 'Black / African American'), ('Hispanic / Latino', 'Hispanic / Latino'), ('Native Hawaiian / Other Pacific Islander', 'Native Hawaiian / Other Pacific Islander'), ('White', 'White')], max_length=50, verbose_name='race')),
                ('bio', models.TextField(blank=True, verbose_name='bio')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is_admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='location.location')),
            ],
            options={
                'ordering': ('nickname',),
            },
        ),
    ]
