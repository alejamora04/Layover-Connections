# Generated by Django 4.1.5 on 2023-02-21 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layoverconnections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
