# Generated by Django 5.1 on 2024-11-26 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohara', '0016_viewcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewcount',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
