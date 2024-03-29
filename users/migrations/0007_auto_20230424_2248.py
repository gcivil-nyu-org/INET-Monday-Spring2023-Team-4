# Generated by Django 3.2 on 2023-04-25 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropoff_locator', '0002_siteschedule_siteseason'),
        ('users', '0006_auto_20230424_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropoff_locator.site')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='sites',
            field=models.ManyToManyField(related_name='hosts', through='users.SiteHost', to='dropoff_locator.Site'),
        ),
    ]
