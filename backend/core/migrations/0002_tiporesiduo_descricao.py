# Generated by Django 5.1.3 on 2024-11-28 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiporesiduo',
            name='descricao',
            field=models.TextField(default='Descrição não fornecida'),
        ),
    ]