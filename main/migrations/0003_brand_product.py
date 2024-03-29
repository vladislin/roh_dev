# Generated by Django 3.0.6 on 2020-07-14 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Назва бренду')),
                ('tag', models.CharField(max_length=50, verbose_name='Тег для HTML')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Назва напою')),
                ('img', models.ImageField(upload_to='production_pictures', verbose_name='Фото напою')),
                ('description', models.CharField(max_length=100, verbose_name='Опис напою')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Brand', verbose_name='Бренд напою')),
            ],
        ),
    ]
