# Generated by Django 5.2.1 on 2025-06-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('guests', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('requests', models.TextField()),
            ],
        ),
    ]
