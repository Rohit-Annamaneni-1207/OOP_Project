# Generated by Django 3.2.7 on 2021-11-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelManagement', '0005_auto_20211129_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='room_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
