from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=80, verbose_name='Заголовок')
    description = models.CharField(max_length=120, verbose_name='Короткий опис')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата публікації')
    text = models.TextField(null=True, verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новини"


class NewsImages(models.Model):
    image = models.ImageField(upload_to='news_picture', verbose_name='Зображення', null=True)
    post = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Фото для новин"

    def __str__(self):
        return str(self.image.url)


class Product(models.Model):
    mi = 'mi'
    roksolana = 'roksolana'
    djerelna = 'djerelna'
    aqua = 'aqua'
    likuvalna = 'likuvalna'

    BRAND_CHOICES = (
        (mi, 'МИ'),
        (roksolana, 'Роксолана'),
        (djerelna, 'Джерельна'),
        (aqua, 'Аква'),
        (likuvalna, 'Лікувальна'),
    )

    title = models.CharField(max_length=60, verbose_name='Назва продукту', help_text='Введіть назву напою')
    brand = models.CharField(max_length=10, choices=BRAND_CHOICES, default=mi, verbose_name='Бренд', help_text='Виберіть бренд напою')
    capacity = models.CharField(max_length=50, verbose_name='Літраж', null=True,
                                help_text="Вкажіть літражі даної продукції (напр. 0.5 л, 1 л, 2 л)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Продукція'


class ProductImages(models.Model):
    image = models.ImageField(upload_to='production_pictures', verbose_name='Зображення', null=True, help_text='Загрузіть фото для напою')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image.url)

    class Meta:
        verbose_name_plural = 'Фото продукції'


class LoadImage(models.Model):
    title = models.CharField(max_length=30, verbose_name='Назва для фото')
    img = models.ImageField(upload_to='home_pictures', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Додайте нове фото для головної сторінки'


class MainImage(models.Model):
    image = models.ForeignKey(LoadImage, related_name='pict', on_delete=models.CASCADE, verbose_name='Виберіть фото')

    def __str__(self):
        return self.image.title

    class Meta:
        verbose_name_plural = 'Виберіть фото на головній сторінці(не додавайте нове фото, змініть уже створене)'




