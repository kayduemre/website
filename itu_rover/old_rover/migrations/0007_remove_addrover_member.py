# Generated by Django 2.0.1 on 2019-01-14 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('old_rover', '0006_member_rover_years'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addrover',
            name='Member',
        ),
    ]