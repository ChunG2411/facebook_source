# Generated by Django 4.1.1 on 2022-10-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interact', '0009_alter_chat_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]