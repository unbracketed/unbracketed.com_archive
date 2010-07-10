from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

from unbracketed.apps.content.models import ProTip, Article


tip_info = {'queryset':ProTip.objects.all()}
articles_archive = {'queryset':Article.objects.all(),
                    'template_name':'content/articles/detail.html'}

urlpatterns = patterns('unbracketed.apps.content.views',
    
    url(r'^tweets/$', 'tweets_archive', name='content_tweets_archive'),
    url(r'^bookmarks/$', 'bookmarks_archive', name='content_bookmarks_archive'),
    
    #
    #Pro Tips
    #
    # Archive
    url(r'^pro-tips/$', 'pro_tips_archive', name='content_pro_tips_archive'),
    # Tip Detail
    url(r'^tip/(?P<slug>.+)/$',
        object_detail,
        tip_info,
        name='content_pro_tips_tip'),
    
    #
    #Articles
    #
    #Archive
    url(r'^writing/articles/$', 'articles_archive',
        name='content_articles_archive'),
    
    #Article
    url(r'^writing/article/(?P<slug>.*)/$', object_detail, articles_archive,
        name='content_article_detail'),
)