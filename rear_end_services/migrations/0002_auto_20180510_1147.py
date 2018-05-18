# Generated by Django 2.0.4 on 2018-05-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rear_end_services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='region',
        ),
        migrations.RemoveField(
            model_name='region',
            name='region_name',
        ),
        migrations.AddField(
            model_name='country',
            name='region_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='region_name',
            field=models.CharField(max_length=100, null=True, verbose_name='地区名'),
        ),
    ]
