# Generated by Django 4.0.4 on 2022-07-23 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_post_create_on_alter_story_create_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 13, 36, 46, 840990)),
        ),
    ]