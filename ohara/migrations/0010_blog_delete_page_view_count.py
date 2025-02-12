# Generated by Django 5.1 on 2024-11-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohara', '0009_page_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Page_view_count',
        ),
    ]
