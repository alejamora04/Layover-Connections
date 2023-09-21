# Generated by Django 4.1.5 on 2023-09-21 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('userimage_1', models.ImageField(default='placeholder.jpg', upload_to='profile_pics')),
                ('userimage_2', models.ImageField(default='placeholder.jpg', upload_to='profile_pics')),
                ('userimage_3', models.ImageField(default='placeholder.jpg', upload_to='profile_pics')),
                ('userimage_4', models.ImageField(default='placeholder.jpg', upload_to='profile_pics')),
                ('hometown', models.CharField(max_length=25, null=True)),
                ('age', models.IntegerField(null=True)),
                ('profile', models.CharField(blank=True, max_length=500)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
