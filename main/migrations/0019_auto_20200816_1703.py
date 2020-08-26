# Generated by Django 3.0.6 on 2020-08-16 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200806_1202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loadimage',
            options={'verbose_name_plural': 'Додайте нове фото для головної сторінки'},
        ),
        migrations.AlterModelOptions(
            name='mainimage',
            options={'verbose_name_plural': 'Виберіть фото на головній сторінці(не додавайте нове фото, змініть уже створене)'},
        ),
        migrations.AlterField(
            model_name='mainimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pict', to='main.LoadImage', verbose_name='Виберіть фото'),
        ),
    ]
