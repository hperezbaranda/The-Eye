# Generated by Django 3.2.11 on 2022-01-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debug', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='Time Stamp')),
                ('view', models.CharField(max_length=30, verbose_name='View')),
                ('exceptionclass', models.CharField(blank=True, max_length=60, verbose_name='Exception Class')),
                ('level', models.CharField(max_length=60, verbose_name='Level')),
                ('message', models.CharField(max_length=200, verbose_name='Exception Message')),
            ],
        ),
        migrations.DeleteModel(
            name='ExceptionLog',
        ),
    ]
