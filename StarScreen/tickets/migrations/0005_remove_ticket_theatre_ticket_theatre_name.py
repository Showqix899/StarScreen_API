# Generated by Django 5.1.4 on 2024-12-10 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Theatre_and_Seats', '0001_initial'),
        ('tickets', '0004_rename_theatre_name_ticket_theatre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='theatre',
        ),
        migrations.AddField(
            model_name='ticket',
            name='theatre_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Theatre_and_Seats.theatre'),
        ),
    ]