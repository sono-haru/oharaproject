# Generated by Django 5.1 on 2024-11-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohara', '0003_remove_blog_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='views',
        ),
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(default='デフォルトのテキスト'),
        ),
    ]
