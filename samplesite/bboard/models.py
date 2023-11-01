from django.db import models


class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name="Товар")
    # null - будет хранить в бд значения Null
    # blank - можно не заполнять данное поле
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    # db_index - создает индекс (дальше мы будем по нему проводить сортировку)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
