# Generated by Django 3.2.15 on 2022-08-16 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='name',
        ),
    ]
