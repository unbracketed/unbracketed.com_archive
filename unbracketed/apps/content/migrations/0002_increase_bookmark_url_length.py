
from south.db import db
from django.db import models
from apps.content.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Bookmark.url'
        # (to signature: django.db.models.fields.URLField(max_length=256, db_index=True))
        db.alter_column('content_bookmark', 'url', orm['content.bookmark:url'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Bookmark.url'
        # (to signature: django.db.models.fields.URLField(max_length=200, db_index=True))
        db.alter_column('content_bookmark', 'url', orm['content.bookmark:url'])
        
    
    
    models = {
        'content.bookmark': {
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_value': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'tags': ('TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'db_index': 'True'})
        },
        'content.status': {
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'meta_value': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'tags': ('TagField', [], {})
        }
    }
    
    complete_apps = ['content']
