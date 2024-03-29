# Generated by Django 3.0.6 on 2021-04-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_mainimage_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainimage',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AddField(
            model_name='mainimage',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Назва для фото'),
        ),
        migrations.AlterField(
            model_name='mainimage',
            name='image',
            field=models.ImageField(blank=True, default=False, null=True, upload_to='home_pictures', verbose_name='Зображення'),
        ),
        migrations.DeleteModel(
            name='LoadImage',
        ),
    ]
