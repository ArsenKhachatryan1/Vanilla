# Generated by Django 4.1.7 on 2023-03-23 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='user_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='user_name',
            new_name='name',
        ),
    ]
