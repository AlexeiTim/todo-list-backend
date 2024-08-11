from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField('Название категории', max_length=255)
    created_at = models.DateTimeField('Дата и время создания категории', auto_now_add=True)
    updated_at = models.DateTimeField('Дата и время последнего обновления категории', auto_now=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField('Название задачи', max_length=255)
    description = models.TextField('Описание задачи')
    priority = models.IntegerField(
        'Приоритет задачи',
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Приоритет должен быть от 1 до 5',
        default=1
    )
    is_completed = models.BooleanField('Статус задачи', default=False)
    dua_date = models.DateTimeField('Дата и время выполнения задачи', null=True, blank=True)
    created_at = models.DateTimeField('Дата и время создания задачи', auto_now_add=True)
    updated_at = models.DateTimeField('Дата и время последнего обновления задачи', auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title

