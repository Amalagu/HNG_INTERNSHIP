# Generated by Django 4.2.5 on 2023-09-08 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_person_current_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='current_day',
            new_name='utc_time',
        ),
        migrations.RemoveField(
            model_name='person',
            name='timestamp',
        ),
    ]