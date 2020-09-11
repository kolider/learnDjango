from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Содержимое")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото")
    is_published = models.BooleanField(default=False, verbose_name="Доступность")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Категория", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
