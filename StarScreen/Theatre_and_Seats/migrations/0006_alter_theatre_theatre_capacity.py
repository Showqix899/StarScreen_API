# Generated by Django 5.1.4 on 2024-12-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Theatre_and_Seats', '0005_rename_theatre_theatre_theatre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theatre',
            name='theatre_capacity',
            field=models.IntegerField(default=200),
        ),
    ]