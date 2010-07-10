from django.contrib.syndication.feeds import Feed
from apps.article.models import Entry, Category
from apps.bookmark.models import Link
from django.db.models import get_model
#from django.contrib.comments.models import FreeComment
from tagging.models import Tag,TaggedItem
from django.core.urlresolvers import reverse

class FeedBase( Feed ):
    """
    Base class providing common title and description path attributes
    """
    title_template = 'feeds/title.html'
    description_template = 'feeds/description.html'

class LatestArticles( FeedBase ):
    """
    Represents a feed of latest articles
    """
    title = 'Unbracketed'
    description = 'Latest Postings from Unbracketed'
    link = "/"
    
    def items(self):
        return Entry.live.all()[:10]
    

class LatestArticlesByCategory( FeedBase ):
    """
    Represents a feed of latest articles in a category
    """
    def get_object(self, bits ):
        if len( bits ) < 1:
            raise ObjectDoesNotExist
        return Category.objects.get(slug=bits[-1])
    
    def title(self, obj ):
        return "Unbracketed %s Entries" % obj.title
    
    def description(self, obj ):
        return "Latest %s Entries on Unbracketed" % obj.title
    
    def link(self, obj ):
        return obj.get_absolute_url()
    
    def items(self, obj ):
        return obj.live_entry_set
        
        
class LatestArticlesByTopic( FeedBase ):
    """
    Represents latest articles by topic (topic is a tag)
    """
    def get_object(self,bits):
        if len( bits ) < 1:
            raise ObjectDoesNotExist
        
        return Tag.objects.get( name=bits[-1] )
    
    def title(self, obj ):
        return "Unbracketed %s Entries" % obj.name
    
    def description(self, obj ):
        return "Latest %s Entries on Unbracketed" % obj.name
    
    def link(self, obj ):
        return reverse( 'blog_tag_list', kwargs={ 'tag' : obj.name }  )
    
    def items(self, obj ):
        return TaggedItem.objects.get_by_model( Entry,obj )
    

#class LatestComments( Feed ):
#    """
#    Represent feed of latest comments on the site
#    """
#    title = "Unbracketed Comments Feed"
#    description = "Latest Comments Made to Entries on Unbracketed"
#    link = "/"
#    title_template = 'feeds/comment_title.html'
#    description_template = 'feeds/comment_description.html'
#    
#    def items(self):
#        return FreeComment.objects.all()[:25]
    
class LatestLinks( FeedBase ):
    """
    Represents a feed of the latest links on the site
    """
    title = "Unbracketed Links Feed"
    description = "Latest Links on Unbracketed: Stuff That Seems Interesting"
    link = "/"
    
    def items(self):
        return Link.objects.all()[:25]
    
