# Generated by Django 2.0.1 on 2018-02-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0008_auto_20180228_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
