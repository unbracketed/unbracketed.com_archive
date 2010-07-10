from django import template
from template_utils.nodes import ContextUpdatingNode
from unipath import FSPath as Path
import pickle

register= template.Library()

class DeliciousDjangoTagsNode( ContextUpdatingNode ):
    
    def get_content( self,context ):
        
        tags_file = open( Path(__file__).parent.parent.child("articles").child("django_delicious_tags").child("django-project-delicious-tags.pickle") )
        tags = pickle.load( tags_file )
        tags_file.close()
        return {'tags' : tags }

@register.tag
def delicious_django_tags( parser, token ):
    return DeliciousDjangoTagsNode()

@register.simple_tag
def  tag_font_size( tags, key ):
    return tags[key]['font_size']