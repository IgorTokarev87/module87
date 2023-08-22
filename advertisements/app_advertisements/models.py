from django.db import models


class Advertisement(models.Model):

    # Название товара
    # CharField - короткое текстовое поле
    # 'Заголовок' - verbose_name - человекочитаемое_название
    title = models.CharField('заголовок', max_length=128)

    # Описание
    # Длинное текстовое поле
    description = models.TextField('описание')

    # Цена
    # Числовое поле с фиксированной точкой
    price = models.DecimalField('цена', max_digits=10, decimal_place=2)

    # Уместен ли торг
    # Булевое поле (логическое)
    auction = models.BooleanField('торг', help_text='Отметьте, если хотите торговаться')

    # Дата публикации
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/обновления + что изменилось
    updated_at = models.DateTimeField(auto_now=True)

    # Продавец (Имя продавца, контакты для связи, отзывы)

    # Фото объявления

    # Рейтинг

    # В продаже/Не в продаже - актуальность