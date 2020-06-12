# Generated by Django 3.0.5 on 2020-06-12 18:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadMacAddresses',
            fields=[
                ('external_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mac_address', models.CharField(max_length=200)),
                ('ipv4_address', models.CharField(max_length=200)),
                ('interface_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitoredInterface',
            fields=[
                ('external_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mac_address', models.CharField(max_length=12)),
                ('ipv4_address', models.CharField(max_length=200)),
                ('interface_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
