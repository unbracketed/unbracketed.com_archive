import re

from django.template import Library, Node, Variable
from django.template.defaultfilters import stringfilter
from django.template.loader import get_template

from unbracketed.apps.content.constants import CONTENT_SOURCE_TWITTER

register = Library()


class TeaserBox(Node):
    def __init__(self, stream_item):
        self.item = Variable(stream_item)
    
    def render(self, context):
        item = self.item.resolve(context).content_object
        context['item'] = item
        t = get_template('content/%s/teaserbox.html'%(item.source,))
        return t.render(context)


@register.tag
def content_teaserbox(parser,token):
    try:
        tag,item = token.split_contents()
        return TeaserBox(item)
    except:
        raise

@register.filter
@stringfilter
def format_tweet(tweet):
    tweet = re.sub(r'(?!<\S)(\w+:\/\/[^<>\s]+\w)', r'<a href="\1">\1</a>', tweet)
    tweet = re.sub(r'(\A|\s)@(\w+)', r'\1<a class="twitter_username" href="http://www.twitter.com/\2">@\2</a>', tweet)
    tweet = re.sub(r'(\A|\s)#(\w+)', r'\1#<a href="http://search.twitter.com/search?q=%23\2">\2</a>', tweet)
    #removed (?!\S) from end of regex
    return tweet 