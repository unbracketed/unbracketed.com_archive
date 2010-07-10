from django.conf.urls.defaults import *
from apps.article.urls.entries import urlpatterns as entry_urlpatterns
from apps.article.urls.categories import urlpatterns as category_urlpatterns
from apps.blog.feeds import *
from apps.blog.views import tag_list
#syndication slugs
feed_info = { 
             'latest'     : LatestArticles,
             'category'   : LatestArticlesByCategory, 
             'topic'      : LatestArticlesByTopic,
             #'comment'    : LatestComments,
             'link'       : LatestLinks
            }


#syndication urls
urlpatterns = patterns( 'django.contrib.syndication.views', 
    url( r'^feed/(?P<url>.*)/$', 'feed', { 'feed_dict' : feed_info }, name="blog_feeds" ),)

#topic based pages (list Entries by tag)
urlpatterns += patterns( '',
                         url( r'^tag/all/$', 'django.views.generic.simple.direct_to_template', { 'template':'blog/topic_cloud.html' }, name="blog_tag_cloud"  ) ,
                         url( r'^tag/(?P<tag>.*)/$', tag_list ,name='blog_tag_list'  ) , )

#urlpatterns += patterns( '',
#                         (r'^comments/postfree/', my_post_free_comment ),
#                         (r'^comments/', include('django.contrib.comments.urls.comments') ), )

urlpatterns += entry_urlpatterns
urlpatterns += category_urlpatterns