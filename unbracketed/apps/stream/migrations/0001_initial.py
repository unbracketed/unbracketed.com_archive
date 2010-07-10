
from south.db import db
from django.db import models
from apps.stream.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Stream'
        db.create_table('stream_stream', (
            ('id', orm['stream.Stream:id']),
            ('content_type', orm['stream.Stream:content_type']),
            ('object_id', orm['stream.Stream:object_id']),
            ('date_created', orm['stream.Stream:date_created']),
            ('date_updated', orm['stream.Stream:date_updated']),
        ))
        db.send_create_signal('stream', ['Stream'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Stream'
        db.delete_table('stream_stream')
        
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'stream.stream': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }
    
    complete_apps = ['stream']
