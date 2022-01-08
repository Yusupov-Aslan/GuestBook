from django.db import models

# Create your models here.
STATUS_CHOICES = [("active", "Активно"), ("blocked", "Заблокировано")]


class Guest(models.Model):
    author_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя автора')
    author_mail = models.EmailField(max_length=100, null=False, blank=False, verbose_name="Почта автора")
    text_notes = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Текст записи')
    status = models.CharField(max_length=20, default='active', choices=STATUS_CHOICES, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    editing_time = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")

    def __str__(self):
        return f"{self.pk}. {self.author_name}: {self.status}"

    class Meta:
        db_table = 'guest'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'