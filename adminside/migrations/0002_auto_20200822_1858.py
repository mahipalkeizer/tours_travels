# Generated by Django 3.1 on 2020-08-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='itinerary_name',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='package',
            name='package_name',
            field=models.CharField(default='NULL', max_length=200),
        ),
    ]
