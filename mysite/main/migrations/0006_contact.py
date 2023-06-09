# Generated by Django 4.1.7 on 2023-03-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='User name')),
                ('user_email', models.EmailField(max_length=254, verbose_name='User email')),
                ('user_message', models.TextField(verbose_name='User message')),
            ],
        ),
    ]
