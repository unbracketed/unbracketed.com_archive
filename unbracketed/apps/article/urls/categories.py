"""
URLs for categories in a weblog.

"""

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list

from apps.article.models import Category
from apps.article.views import category_detail


urlpatterns = patterns('',
                       url(r'^$',
                           object_list,
                           { 'queryset': Category.objects.all() },
                           name='article_category_list'),
                       url(r'^(?P<slug>[-\w]+)/$',
                           category_detail,
                           name='article_category_detail'),
                       )
