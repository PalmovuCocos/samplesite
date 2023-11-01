from django.db import models


class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name="Товар")
    # значение protect защищает записи от каскадного удаления
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name="Рубрика")
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


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


