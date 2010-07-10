from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models



class WritingStreamManager(models.Manager):
    '''Model manager for the content stream
    '''
    def get_query_set(self):
        #TODO here due to circular import
        from unbracketed.apps.content.models import ProTip, Article
        cta = ContentType.objects.get_for_model(Article)
        ctp = ContentType.objects.get_for_model(ProTip)
        return super(WritingStreamManager,self).get_query_set().filter(
            content_type__pk__in=[cta.id, ctp.id]
        )
        
    
class Stream(models.Model):
    """Maintains a chronological list of content items"""
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    date_created = models.DateTimeField(default=datetime.now)
    date_updated = models.DateTimeField(null=True)
    
    objects = models.Manager()
    writing = WritingStreamManager()
    
    class Meta:
        ordering = ('-date_created',)
    
    def __unicode__(self):
        return unicode(self.content_object)
        
    
    
    

