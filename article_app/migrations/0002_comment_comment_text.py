# Generated by Django 4.2 on 2024-04-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(default='', verbose_name='Comment'),
        ),
    ]
