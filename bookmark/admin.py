from django.contrib import admin
from .models import Bookmark
# Register your models here.


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'url']


admin.site.register(Bookmark, BookmarkAdmin)

