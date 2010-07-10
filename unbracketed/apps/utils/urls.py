from django.conf.urls.defaults import *
from apps.utils.views import apply_markdown

urlpatterns = patterns( '',
    ( r'^markup/markdown', apply_markdown ),
    )

