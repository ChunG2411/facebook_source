# Generated by Django 4.0.4 on 2022-07-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_story_create_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=255),
        ),
    ]
