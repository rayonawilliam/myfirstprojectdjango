# Generated by Django 3.2.2 on 2021-05-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_bookcall_registeruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookadvisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='bookcall',
        ),
    ]
