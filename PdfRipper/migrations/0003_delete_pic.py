# Generated by Django 3.2.15 on 2022-08-16 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PdfRipper', '0002_rename_venue_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pic',
        ),
    ]