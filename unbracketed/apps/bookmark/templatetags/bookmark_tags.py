from django import template
from django.core.urlresolvers import reverse
from django.template import resolve_variable
from bookmark.models import Link

register = template.Library()

class LinksNode(template.Node):
    '''
    adds a 'bookmark_links' variable to the render context
    which is a list of all Links
    '''    
    def render(self, context):
        context['bookmark_links'] = Link.objects.all()
        return ''
    

@register.tag    
def bookmark_links_to_context( parser, token ):
    '''
    adds the Links queryset containing all Links to the render context 
    '''
    return LinksNode()
