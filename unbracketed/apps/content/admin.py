from django.contrib import admin
from markitup.widgets import MarkItUpWidget

from unbracketed.apps.content.models import Bookmark, Status, ProTip, Article


#TODO: hide date modified and date created 
class ContentAdmin:
    pass

class BookmarkAdmin(admin.ModelAdmin):
    pass


class StatusAdmin(admin.ModelAdmin):
    pass

class ProTipAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("description",)}
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'explanation_raw':
            kwargs['widget'] = MarkItUpWidget(attrs={'class': 'vLargeTextField'})
        return super(ProTipAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class ArticleAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("title",)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'body':
            kwargs['widget'] = MarkItUpWidget(attrs={'class': 'vLargeTextField'})
        return super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Bookmark,BookmarkAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(ProTip,ProTipAdmin)
admin.site.register(Article,ArticleAdmin)