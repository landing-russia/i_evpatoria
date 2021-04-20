from django.db import models


class Exscursion(models.Model):
    TYPES = (
        ('group', 'Групповая'),
        ('individual', 'Индивидуальная'),
    )

    name = models.CharField(max_length=255, verbose_name='Название экскурсии')
    description = models.TextField(blank=True, verbose_name='Описание')
    location = models.CharField(max_length=255, verbose_name='Локация', null=True, blank=True)
    duration = models.CharField(max_length=255, verbose_name='Длительность', null=True, blank=True)
    max_people_count = models.CharField(max_length=255, verbose_name='Кол-во человек', null=True, blank=True)
    price = models.CharField(max_length=255, verbose_name='Стоимость', null=True, blank=True)
    photo = models.ImageField(upload_to='excursions_photos', verbose_name='Фото', null=True, blank=True)
    type = models.CharField(max_length=10, choices=TYPES, verbose_name='Тип', default='group')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экскурсию'
        verbose_name_plural = 'Экскурсии'
        ordering = ['-created_at']
