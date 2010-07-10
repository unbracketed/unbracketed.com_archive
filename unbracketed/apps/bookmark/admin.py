from django.contrib import admin
from apps.bookmark.models import Link

class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'pub_date'
    #fields = (
    #    ('Metadata', { 'fields':
    #                   ('title', 'slug', 'pub_date', 'posted_by', 'enable_comments') }),
    #    ('Link', { 'fields':
    #              ('url', 'description', 'tags', 'via_name', 'via_url') }),
    #    )
    list_display = ('title', 'enable_comments')
    search_fields = ('title', 'description')

admin.site.register(Link,LinkAdmin)