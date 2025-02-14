# Generated by Django 5.1.4 on 2024-12-10 13:56

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('show_start_time', models.DateTimeField()),
                ('show_end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('theatre_name', models.CharField(blank=True, max_length=100, null=True)),
                ('theatre_location', models.CharField(blank=True, max_length=300, null=True)),
                ('theatre_capacity', models.IntegerField(default=20)),
                ('screen_types', models.CharField(choices=[('Standard', 'Standard Screen'), ('IMAX', 'IMAX Screen'), ('Dolby', 'Dolby Cinema Screen'), ('3D', '3D Screen'), ('4DX', '4DX Screen')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('seat_no', models.CharField(blank=True, max_length=5, null=True)),
                ('seat_catagory', models.CharField(blank=True, max_length=20, null=True)),
                ('is_available', models.BooleanField(default=False)),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Theatre_and_Seats.theatre')),
            ],
        ),
    ]
