# Generated by Django 2.0 on 2019-06-10 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_create_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
