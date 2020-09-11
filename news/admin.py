from django.contrib import admin

from news.models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_at', 'update_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('content', )
    list_filter = ('category', 'is_published')
    list_editable = ('is_published',)

admin.site.register(News, NewsAdmin)

admin.site.register(Category)
