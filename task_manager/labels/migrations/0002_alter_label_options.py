# Generated by Django 5.0 on 2024-01-23 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': 'Метка', 'verbose_name_plural': 'Метки'},
        ),
    ]
