# Generated by Django 2.0.5 on 2018-09-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codestudy', '0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.CreateModel(
            name='Root',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'root',
                'managed': False,
            },
        ),
    ]
