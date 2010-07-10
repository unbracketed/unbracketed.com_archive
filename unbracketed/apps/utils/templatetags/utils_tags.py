from django import template
from unbracketed.apps.utils.nodes import FlexGenericContentNode

register = template.Library()

def do_generic_object_list(parser, token):
    """
    Retrieves the latest ``num`` objects from a given model, in that
    model's default ordering, and stores them in a context variable.
    
    You can specify 'all' for ``num`` to retrieve the all() queryset.
    
    Syntax::
    
        {% get_latest_objects [app_name].[model_name] [num] as [varname] %}
    
    Example::
    
        {% get_latest_objects comments.freecomment 5 as latest_comments %}
    
    """
    bits = token.contents.split()
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'%s' tag takes four arguments" % bits[0])
    if bits [3] != 'as':
        raise template.TemplateSyntaxError("third argument to '%s' tag must be 'as'" % bits[0])
    return FlexGenericContentNode(bits[1], bits[2], bits[4])

register.tag( 'generic_object_list', do_generic_object_list )


