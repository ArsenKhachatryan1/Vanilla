# Generated by Django 4.1.7 on 2023-03-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.CharField(max_length=50, verbose_name='Price')),
                ('img', models.ImageField(upload_to='images', verbose_name='Small image')),
                ('img_big', models.ImageField(upload_to='images', verbose_name='Big image')),
            ],
        ),
    ]
