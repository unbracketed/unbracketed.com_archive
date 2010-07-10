from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from markdown import markdown
from tagging.fields import TagField
from tagging.utils import parse_tag_input 

from unbracketed.apps.content.constants import (CONTENT_SOURCE_CHOICES,
                                                CONTENT_SOURCE_TWITTER,
                                                CONTENT_PUBLISH_STATUS_CHOICES,
                                                CONTENT_PUBLISH_STATUS_DRAFT,)
from unbracketed.apps.stream.receivers import add_stream_item
#from unbracketed.apps.utils.text import format_rst


#TODO use extensions datetime fields
class Content(models.Model):
    """Base Content Type"""
    active = models.NullBooleanField()
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(null=True)
    #TODO:
    #date_published = models.DateTimeField(u'Date posted', default=datetime.datetime.today)
    source = models.CharField(max_length=50,choices=CONTENT_SOURCE_CHOICES)
    source_id = models.CharField(max_length=256,blank=True)
    meta_value = models.CharField(max_length=256,blank=True)
    tags = TagField()
        
    class Meta:
        abstract = True
        ordering = ['-date_created',]
        
    def get_tag_list(self):
        return parse_tag_input(self.tags)
        
    def feed_title(self):
        pass
    
    def feed_body(self):
        pass
        

    
class BookmarkBase(Content):
    """Base class for Bookmarks."""
    title = models.CharField(max_length=256)
    url = models.URLField(db_index=True,max_length=256)
    description = models.TextField(blank=True)
    
    
    class Meta:
        abstract = True
        ordering = ('-date_created','-date_modified')
        
    def __unicode__(self):
        return u'%s: %s' % (self.get_source_display(),self.title)
        
    def save(self,force_insert=False,force_update=False):
        if not len(self.title):
            self.title = self.url
        super(BookmarkBase,self).save(force_insert,force_update)
    

class Bookmark(BookmarkBase):
    """Bookmarks internal to the site"""
    pass

    


class StatusBase(Content):
    """Base class for status items"""
    message = models.CharField(max_length=500)
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return u"%s: %s" % (self.get_source_display(), self.message)
    

class TweetStatusManager(models.Manager):
    """Work with only Tweet Statuses"""
    def get_query_set(self):
         return super(TweetStatusManager, self).get_query_set().filter(source=CONTENT_SOURCE_TWITTER)

    
class Status(StatusBase):
    """A status message private to this site"""
    
    objects = models.Manager()
    tweets = TweetStatusManager()
    
    class Meta:
        verbose_name = 'Status Updates'
        verbose_name_plural = 'Status Updates'
        ordering = ['-date_created',]
        
    def __unicode__(self):
        return self.message
    
    def source_url(self):
        if self.source == CONTENT_SOURCE_TWITTER:
            return "http://twitter.com/unbracketed/statuses/%s" % (self.source_id,)
            

class ProTip(Content):
    """A tip, technique, or best practice"""
    
    description = models.CharField(max_length=256)
    slug = models.SlugField(blank=True,null=True)
    #TODO deprecate the denorm field
    explanation_raw = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('content_pro_tips_tip',[self.slug],)
    
    def __unicode__(self):
        return self.description
    
    def save(self):
        #self.explanation = format_rst(self.explanation_raw)
        self.explanation = markdown(self.explanation_raw,['codehilite'])
        super(ProTip,self).save()
        
    def feed_title(self):
        return self.description
    
    def feed_body(self):
        return self.explanation
        
        
class Article(Content):
    """Article"""

    
    #MARKUP_MARKDOWN = 1
    #MARKUP_MARKDOWN_CODEHILITE = 2
    #MARKUP_REST = 3
    #MARKUP_TEXTILE = 4
    #MARKUP_CHOICES = (
    #    (MARKUP_MARKDOWN, 'Markdown'),
    #    (MARKUP_MARKDOWN_CODEHILITE, 'Markdown + Codehilite' ),
    #    (MARKUP_REST, 'ReStructured Text'),
    #    (MARKUP_TEXTILE, 'Textile'),
    #)
    
    # Metadata.
    author = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text=u'Used in the URL of the entry. Must be unique for the publication date of the entry.')
    status = models.CharField(choices=CONTENT_PUBLISH_STATUS_CHOICES,
        default=CONTENT_PUBLISH_STATUS_DRAFT,
        help_text=u'Only entries with "live" status will be displayed publicly.',
        max_length=10)
    
    
    body = models.TextField()
    #body_html = models.TextField(editable=False, blank=True)
    excerpt = models.TextField(blank=True, null=True)
    #excerpt_html = models.TextField(blank=True, null=True, editable=False)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    #date_published = models.DateTimeField(u'Date posted', default=datetime.datetime.today)
    #markup_filter = models.IntegerField( choices=MARKUP_CHOICES,default=MARKUP_MARKDOWN )
    
    @property
    def body_display(self):
        return markdown(self.body,['codehilite'])
    
    class Meta:
        get_latest_by = 'date_modified'
        ordering = ['-date_created']
        verbose_name_plural = 'Articles'
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('content_article_detail',[self.slug],)
        
    def get_absolute_url(self):
        return ('content_article_detail', (), {'slug':self.slug})
    get_absolute_url = models.permalink(get_absolute_url)
    
    def feed_title(self):
        return self.title
    
    def feed_body(self):
        return markdown(self.body)
    

post_save.connect(add_stream_item, sender=Bookmark)
post_save.connect(add_stream_item, sender=Status)
post_save.connect(add_stream_item, sender=ProTip)
post_save.connect(add_stream_item, sender=Article)
