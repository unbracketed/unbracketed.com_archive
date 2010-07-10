from django.db.models import get_model
from django import template
from tagging.models import Tag
from django.core.urlresolvers import reverse
from django.template.defaultfilters import stringfilter

register = template.Library()

def sort_tags_by_count( item ):
    return item.count

class TopTagsForModelNode(template.Node):
    def __init__(self, model, context_var, num_tags ):
        self.model = model
        self.context_var = context_var
        self.num_tags = int(num_tags)

    def render(self, context):
        model = get_model(*self.model.split('.'))
        if model is None:
            raise TemplateSyntaxError(_('tags_for_model tag was given an invalid model: %s') % self.model)
        tags = Tag.objects.usage_for_model(model, counts=True)
        tags.sort( key=sort_tags_by_count, reverse=True )
        for tag in tags:
            _url = 'topic/%s' % tag.name.lower()
            tag.feed_url = reverse('blog_feeds', kwargs={'url': _url })
        
        context[self.context_var] = tags[:self.num_tags]
        return ''


def do_top_tags_for_model(parser, token):
    """
    Retrieves a list of the most popular ``Tag`` objects associated with a given model
    and stores them in a context variable.

    Usage::

       {% top_tags_for_model [model] as [varname] [num]  %}

    The model is specified in ``[appname].[modelname]`` format.
    ``[num]`` is the number of top tags to return

    Examples::

       {% top_tags_for_model products.Widget as widget_tags 5 %}

    """
    bits = token.contents.split()
    len_bits = len(bits)
    if len_bits != 5:
        raise TemplateSyntaxError(_('%s tag requires four arguments') % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError(_("second argument to %s tag must be 'as'") % bits[0])
    
    return TopTagsForModelNode(bits[1], bits[3], bits[4] )
    
register.tag( 'top_tags_for_model', do_top_tags_for_model )



@register.filter
@stringfilter
def tag_syntax( tag ):
    if ' ' in tag:
        return '"%s"' % tag
    else:
        return tag