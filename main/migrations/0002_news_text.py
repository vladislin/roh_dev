# Generated by Django 3.0.6 on 2020-07-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
