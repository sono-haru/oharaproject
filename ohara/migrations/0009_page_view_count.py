# Generated by Django 5.1 on 2024-11-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohara', '0008_keiziban_post_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page_view_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
