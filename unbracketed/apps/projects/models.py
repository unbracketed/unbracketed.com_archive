from django.db import models
from unbracketed.apps.utils.text import format_rst

class Project(models.Model):
    """Provides home pages for creative and coding projects I'm working on"""
    
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    repository_url = models.CharField(max_length=128,blank=True)
    tease = models.CharField(max_length=500,blank=True)
    description_raw = models.TextField(blank=True)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        """Convert the description into HTML"""
        self.description = format_rst(self.description_raw)
        super(Project,self).save()

    
