# Generated by Django 2.2.5 on 2019-10-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0002_auto_20191013_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.CharField(default='Null', max_length=50),
        ),
    ]