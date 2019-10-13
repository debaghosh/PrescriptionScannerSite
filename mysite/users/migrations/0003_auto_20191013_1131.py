# Generated by Django 2.2.5 on 2019-10-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191012_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], default='Usertype', max_length=7),
        ),
    ]
