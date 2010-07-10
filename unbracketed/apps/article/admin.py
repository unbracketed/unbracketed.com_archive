from django.contrib import admin
from apps.article.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'pub_date'
    #fields = (
    #    ('Metadata', { 'fields':
    #                   ('title', 'slug', 'pub_date', 'author', 'status', 'featured', 'enable_comments') }),
    #    ('Entry', { 'fields':
    #                ('markup_filter','excerpt', 'body') }),
    #    ('Categorization', { 'fields':
    #                         ('tags', 'categories') }),
    #    )
    list_display = ('title', 'pub_date', 'author', 'status', 'enable_comments', '_get_comment_count')
    list_filter = ('status', 'categories')
    search_fields = ('excerpt', 'body', 'title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)


