# Generated by Django 4.2.5 on 2023-09-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
