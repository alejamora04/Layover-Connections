# Generated by Django 4.1.5 on 2023-02-21 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layoverconnections', '0004_alter_profile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='profile',
            name='hometown',
            field=models.CharField(max_length=25, null=True),
        ),
    ]