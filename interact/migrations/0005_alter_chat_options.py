# Generated by Django 4.0.4 on 2022-08-03 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interact', '0004_chat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ['-create_on']},
        ),
    ]
