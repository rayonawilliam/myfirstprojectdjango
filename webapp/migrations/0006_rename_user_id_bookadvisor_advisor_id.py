# Generated by Django 3.2.2 on 2021-05-14 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_booking_time_bookadvisor_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookadvisor',
            old_name='user_id',
            new_name='advisor_id',
        ),
    ]