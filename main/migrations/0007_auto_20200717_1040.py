# Generated by Django 3.0.6 on 2020-07-17 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200717_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Новини'},
        ),
        migrations.AlterModelOptions(
            name='newsimages',
            options={'verbose_name_plural': 'Фото для новин'},
        ),
    ]
