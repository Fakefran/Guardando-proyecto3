# Generated by Django 5.0 on 2024-01-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_rename_profesio_profesor_profesion'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregable',
            name='chek',
            field=models.BooleanField(default=False),
        ),
    ]
