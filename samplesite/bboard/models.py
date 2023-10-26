from django.db import models


class Bd(models.Model):
    title = models.CharField(max_length=50)
    # null - будет хранить в бд значения Null
    # blank - можно не заполнять данное поле
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    # db_index - создает индекс (дальше мы будем по нему проводить сортировку)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
