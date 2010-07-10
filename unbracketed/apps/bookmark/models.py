"""
Provides a bookmarks / links feature commonly found on blogs
Largely based on work from James Bennett's coltrane app
"""
from django.db import models
from django.contrib.auth.models import User
import datetime
from tagging.fields import TagField
#from comment_utils.managers import CommentedObjectManager

class Link(models.Model):
    """
    A link posted to the weblog.
    
    Denormalized in the same fashion as the Entry model, in order to
    allow text-to-HTML conversion to be performed on the
    ``description`` field.
    
    """
    # Metadata.
    enable_comments = models.BooleanField(default=True)
    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.datetime.today)
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text=u'Must be unique for the publication date.')
    title = models.CharField(max_length=250)
    
    # The actual link bits.
    description = models.TextField(blank=True, null=True)
    description_html = models.TextField(editable=False, blank=True, null=True)
    via_name = models.CharField(u'Via', max_length=250, blank=True, null=True,
                                help_text=u'The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField('Via URL', verify_exists=False, blank=True, null=True,
                              help_text=u'The URL of the site where you spotted the link. Optional.')
    tags = TagField()
    url = models.URLField('URL', unique=True, verify_exists=False)
    
    #objects = CommentedObjectManager()
    
    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-pub_date']
    
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return ('bookmark_link_detail', (), { 'year': self.pub_date.strftime('%Y'),
                                              'month': self.pub_date.strftime('%b').lower(),
                                              'day': self.pub_date.strftime('%d'),
                                              'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

