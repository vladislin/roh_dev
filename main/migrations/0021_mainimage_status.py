# Generated by Django 3.0.6 on 2021-04-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210329_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainimage',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Актвине фото'),
        ),
    ]