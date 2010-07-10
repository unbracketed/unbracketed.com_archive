from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template

from unbracketed.apps.content.urls import urlpatterns as content_patterns
from unbracketed.apps.stream.feeds import WritingFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','unbracketed.apps.blog.views.index',name="home_page"),
    (r'^projects/', include('unbracketed.apps.projects.urls')),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt'} ),
    
    #markitup preview
    url(r'^markitup/', include('markitup.urls')),
    
    
    (r'^admin/(.*)', admin.site.root),
    
)

feed_info = {'latest':WritingFeed}
#
##syndication urls
urlpatterns += patterns( 'django.contrib.syndication.views', 
    url( r'^feed/(?P<url>.*)/$', 'feed', {'feed_dict':feed_info}, name="feeds" ),)

urlpatterns += content_patterns

#STATIC MEDIA SERVING FOR RUNSERVER MODE
#** DEBUG MODE ONLY**    
from django.views.static import serve
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^site_media/(?P<path>.*)$',
             serve,
             {'document_root' : settings.MEDIA_ROOT }),
            )
