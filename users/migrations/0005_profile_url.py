# Generated by Django 3.2 on 2023-04-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
