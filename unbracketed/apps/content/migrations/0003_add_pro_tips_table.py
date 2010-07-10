
from south.db import db
from django.db import models
from unbracketed.apps.content.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'ProTip'
        db.create_table('content_protip', (
            ('id', orm['content.protip:id']),
            ('active', orm['content.protip:active']),
            ('date_created', orm['content.protip:date_created']),
            ('date_modified', orm['content.protip:date_modified']),
            ('source', orm['content.protip:source']),
            ('source_id', orm['content.protip:source_id']),
            ('meta_value', orm['content.protip:meta_value']),
            ('tags', orm['content.protip:tags']),
            ('description', orm['content.protip:description']),
            ('explanation_raw', orm['content.protip:explanation_raw']),
            ('explanation', orm['content.protip:explanation']),
        ))
        db.send_create_signal('content', ['ProTip'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'ProTip'
        db.delete_table('content_protip')
        
        
    
    
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
        'content.protip': {
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'explanation_raw': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_value': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'tags': ('TagField', [], {})
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
