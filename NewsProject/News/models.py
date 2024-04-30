from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Заголовок')
    content = models.TextField(blank=True, verbose_name = 'Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')
    photo = models.ImageField(upload_to='media/%Y/%M/%D', verbose_name = 'Фото')
    is_published = models.BooleanField(default=True, verbose_name = 'Публикация')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']