from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic.list_detail import object_list

from unbracketed.apps.content.models import Status, Bookmark, ProTip, Article


def simple_archive_view(request,queryset,template_name,
                        extra_context={},paginate_by=15):
    return object_list(request,
                       queryset,
                       paginate_by=paginate_by,
                       template_name=template_name,
                       extra_context=extra_context)


def tweets_archive(request):
    template_name = 'content/twitter/tweet_page.html' if request.is_ajax() \
                    else 'content/twitter/archive.html'
    #import pdb; pdb.set_trace()
    TWEET_PAGE_CACHE_KEY = 'twitter_archive_page_%s' % request.GET.get('page')
    
    tweet_page = cache.get(TWEET_PAGE_CACHE_KEY)
    if tweet_page:
        #print 'got from cacheS'
        return tweet_page
        
    rendered = simple_archive_view(request,
                       Status.objects.all(),
                       template_name,
                       extra_context={
                         'archive_url':reverse('content_tweets_archive'),
                         'container':'twitter'
                       })
    
    cache.set(TWEET_PAGE_CACHE_KEY, rendered)
    return rendered
    

def bookmarks_archive(request):
    template_name = 'content/delicious/delicious_page.html' if request.is_ajax() \
                    else 'content/delicious/archive.html'
    
    return simple_archive_view(request,
                       Bookmark.objects.all(),
                       template_name,
                       extra_context={
                         'archive_url':reverse('content_bookmarks_archive'),
                         'container':'delicious'
                       })
    
def pro_tips_archive(request):
    template_name = 'content/pro-tips/pro-tips_page.html' if request.is_ajax() \
                    else 'content/pro-tips/archive.html'
    
    return simple_archive_view(request,
                       ProTip.objects.all(),
                       template_name,
                       extra_context={
                         'archive_url':reverse('content_pro_tips_archive'),
                         'container':'pro-tips'
                       })
    


def articles_archive(request):
    template_name = 'content/articles/page.html' if request.is_ajax() \
                    else 'content/articles/archive.html'
    
    return simple_archive_view(request,
                       Article.objects.all(),
                       template_name,
                       extra_context={
                         'archive_url':reverse('content_articles_archive'),
                         'container':'article'
                       })


def article_detail(request):
    pass

