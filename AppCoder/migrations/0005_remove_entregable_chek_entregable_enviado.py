# Generated by Django 5.0 on 2024-01-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_entregable_chek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregable',
            name='chek',
        ),
        migrations.AddField(
            model_name='entregable',
            name='enviado',
            field=models.BooleanField(default=True),
        ),
    ]