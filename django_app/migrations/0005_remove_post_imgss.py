# Generated by Django 3.1.1 on 2021-01-29 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_post_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imgss',
        ),
    ]