from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from tagging.models import TaggedItem,Tag

#from apps.article.models import Entry
from unbracketed.apps.stream.models import Stream


def index(request):
    #TODO error handling
    items = Stream.objects.all()[:6]
    return render_to_response('index.html',locals(),context_instance=RequestContext(request))

def tag_list( request, tag ):
    '''
    renders a list of Entry objects that are tagged with tag
    '''
    return render_to_response( 'blog/topic_list.html', { 'topic_list' : TaggedItem.objects.get_by_model( Entry,Tag.objects.get(name=tag) ), 'tag_text' : tag }, context_instance=RequestContext(request) )
    

#def my_post_free_comment(request):
#    '''
#    this view is used to redirect back to the Entry detail page on a successful Free Comment addition
#    '''
#    if request.has_key('url') and not request.has_key('preview'):
#        response = post_free_comment(request)
#        
#        # Check there's a url to redirect to, and that post_free_comment worked
#        if len(request['url'].strip()) > 0 and isinstance(response, HttpResponseRedirect):
#            return HttpResponseRedirect(request['url'])
#        
#        # Fall back on the default post_free_comment response
#        return response
#    
#    return post_free_comment(request)

