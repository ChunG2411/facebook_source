# Generated by Django 4.0.4 on 2022-07-18 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 18, 17, 0, 31, 353449)),
        ),
    ]