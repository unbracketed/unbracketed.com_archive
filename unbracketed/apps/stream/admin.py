from django.contrib import admin
from unbracketed.apps.stream.models import Stream


class StreamAdmin(admin.ModelAdmin):
    pass



admin.site.register(Stream,StreamAdmin)
