
from south.db import db
from django.db import models
from apps.content.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Status'
        db.create_table('content_status', (
            ('id', orm['content.Status:id']),
            ('active', orm['content.Status:active']),
            ('date_created', orm['content.Status:date_created']),
            ('date_modified', orm['content.Status:date_modified']),
            ('source', orm['content.Status:source']),
            ('source_id', orm['content.Status:source_id']),
            ('meta_value', orm['content.Status:meta_value']),
            ('tags', orm['content.Status:tags']),
            ('message', orm['content.Status:message']),
        ))
        db.send_create_signal('content', ['Status'])
        
        # Adding model 'Bookmark'
        db.create_table('content_bookmark', (
            ('id', orm['content.Bookmark:id']),
            ('active', orm['content.Bookmark:active']),
            ('date_created', orm['content.Bookmark:date_created']),
            ('date_modified', orm['content.Bookmark:date_modified']),
            ('source', orm['content.Bookmark:source']),
            ('source_id', orm['content.Bookmark:source_id']),
            ('meta_value', orm['content.Bookmark:meta_value']),
            ('tags', orm['content.Bookmark:tags']),
            ('title', orm['content.Bookmark:title']),
            ('url', orm['content.Bookmark:url']),
            ('description', orm['content.Bookmark:description']),
        ))
        db.send_create_signal('content', ['Bookmark'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Status'
        db.delete_table('content_status')
        
        # Deleting model 'Bookmark'
        db.delete_table('content_bookmark')
        
    
    
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
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'db_index': 'True'})
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
