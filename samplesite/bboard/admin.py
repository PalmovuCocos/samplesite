from django.contrib import admin

from bboard.models import Bd


class BdAdmin(admin.ModelAdmin):  # класс-редактор
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )


admin.site.register(Bd, BdAdmin)
