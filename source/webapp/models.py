from django.db import models
from static.classes.static import Static
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200, null=False,
                             blank=False, verbose_name="Заголовок")
    description = models.TextField(
        max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=200, null=False, blank=False,
                              choices=Static.choices, default='new', verbose_name="Статус")
    is_deleted = models.BooleanField(
        verbose_name='удалено', null=False, default=False)
    completion_date = models.DateField(
        null=True, blank=True, verbose_name="Выполнить до")
    deleted_at = models.DateField(
        null=True, default=None, verbose_name="Дата удаления")

    def __str__(self):
        return f"{self.title} - {self.description}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
