# Generated by Django 3.2 on 2023-04-29 06:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dropoff_locator', '0005_auto_20230429_0103'),
        ('users', '0007_auto_20230424_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Sent', 'Sent'), ('OpenNotScheduled', 'OpenNotScheduled'), ('Scheduled', 'Scheduled'), ('Rejected', 'Rejected'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Sent', max_length=25)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='users.profile')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receives', to='users.profile')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropoff_locator.site')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('read', models.BooleanField(default=False)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor_request.request')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
