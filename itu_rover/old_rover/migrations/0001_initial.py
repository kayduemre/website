# Generated by Django 2.0.1 on 2019-01-13 15:16

from django.db import migrations, models
import django.db.models.deletion
import old_rover.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(db_index=True, max_length=25, verbose_name='first name')),
                ('last_name', models.CharField(max_length=25, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('photo', models.ImageField(upload_to=old_rover.utils.get_upload_path, verbose_name='photo')),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='phone number')),
                ('is_retired', models.BooleanField(default=False, verbose_name='is member retired?')),
                ('description', models.CharField(blank=True, max_length=75, verbose_name='description (e.g. department)')),
            ],
            options={
                'abstract': False,
                'ordering': ('first_name', 'last_name'),
            },
        ),
        migrations.CreateModel(
            name='MembersPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal', models.FileField(blank=True, upload_to='documents/team')),
                ('team_photo', models.ImageField(blank=True, upload_to='images/members')),
            ],
            options={
                'verbose_name': 'Members Page',
                'verbose_name_plural': 'Members Page',
            },
        ),
        migrations.CreateModel(
            name='SubTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='subteam name')),
                ('leader', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leader_of', to='old_rover.Member', verbose_name='subteam leader')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TeamAdvisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(db_index=True, max_length=25, verbose_name='first name')),
                ('last_name', models.CharField(max_length=25, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('photo', models.ImageField(upload_to=old_rover.utils.get_upload_path, verbose_name='photo')),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='phone number')),
                ('is_retired', models.BooleanField(default=False, verbose_name='is member retired?')),
                ('description', models.CharField(max_length=75, verbose_name='description (e.g. department)')),
            ],
            options={
                'abstract': False,
                'ordering': ('first_name', 'last_name'),
            },
        ),
        migrations.CreateModel(
            name='TeamLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leader', to='old_rover.Member', verbose_name='team leader')),
            ],
            options={
                'verbose_name': 'team leader',
                'verbose_name_plural': 'team leader',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='subteam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='old_rover.SubTeam', verbose_name='subteam of member'),
        ),
    ]
