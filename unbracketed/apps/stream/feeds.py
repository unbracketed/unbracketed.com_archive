from django.contrib.syndication.feeds import Feed

from unbracketed.apps.stream.models import Stream 

class FeedBase(Feed):
    """Base class providing common title and description path attributes
    """
    title_template = 'feeds/title.html'
    description_template = 'feeds/description.html'


class WritingFeed(FeedBase):
    """Represents a feed of latest articles
    """
    title = 'Unbracketed'
    description = 'Recent Items'
    link = "/"
    
    def items(self):
        return Stream.writing.all()[:10]
    
    def item_link(self, item):
        return item.content_object.get_absolute_url()