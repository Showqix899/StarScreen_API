# Generated by Django 5.1.4 on 2024-12-19 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Theatre_and_Seats', '0007_remove_seat_seat_catagory_alter_seat_is_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
