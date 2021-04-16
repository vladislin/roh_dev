# Generated by Django 3.0.6 on 2021-03-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200816_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('mi', 'МИ'), ('roksolana', 'Роксолана'), ('djerelna', 'Джерельна'), ('aqua-daily', 'Аква Daily'), ('aqua-fruit', 'Аква Fruit'), ('likuvalna', 'Лікувальна')], default='mi', help_text='Виберіть бренд напою', max_length=10, verbose_name='Бренд'),
        ),
    ]