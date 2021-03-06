# Generated by Django 3.2.11 on 2022-01-21 05:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.TextField()),
                ('path', models.TextField()),
                ('element', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.UUIDField(default=uuid.uuid4)),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eye.dataevent')),
            ],
        ),
    ]
