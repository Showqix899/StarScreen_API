# Generated by Django 5.1.4 on 2024-12-19 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_remove_ticket_created_by_ticket_is_bought'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='is_bought',
            new_name='is_booked',
        ),
    ]
