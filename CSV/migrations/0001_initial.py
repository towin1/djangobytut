# Generated by Django 3.2.15 on 2022-08-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PDFfile', models.FileField(upload_to='PDF/')),
            ],
        ),
    ]