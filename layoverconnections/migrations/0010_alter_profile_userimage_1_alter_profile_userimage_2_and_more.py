# Generated by Django 4.1.5 on 2023-03-24 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layoverconnections', '0009_alter_profile_userimage_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userimage_1',
            field=models.ImageField(default='placeholder.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userimage_2',
            field=models.ImageField(default='placeholder.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userimage_3',
            field=models.ImageField(default='placeholder.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userimage_4',
            field=models.ImageField(default='placeholder.jpg', upload_to='profile_pics'),
        ),
    ]