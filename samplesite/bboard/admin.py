from django.contrib import admin

from bboard.models import *


class BdAdmin(admin.ModelAdmin):  # класс-редактор
    list_display = ('title', 'content', 'price', 'published', 'rubric') # вывод полей на странице с списком записей
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )


admin.site.register(Rubric)
admin.site.register(Bd, BdAdmin)
