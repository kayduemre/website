# Generated by Django 2.0.1 on 2019-01-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old_rover', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddRover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rover_name', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ('rover_name',),
            },
        ),
    ]
