# Generated by Django 4.2.5 on 2023-09-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_person_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='current_day',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
